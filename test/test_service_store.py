import pytest
from server.ServiceStore import *

TEST_ELEMENT_NAME = "test_element"
TEST_ELEMENT_DATA = {"Value":"1", "Color":"red"}

TEST_CONTROL_NAME = "test_control"
TEST_CONTROL_DATASET = {"value":{"desc":"Value to set the light", "type":"number"},
                        "color":{"desc":"Color to set the light", "type":"string"}}
TEST_CONTROL_COLOR_VAL = "blue"
TEST_CONTROL_VALUE_VAL = "1"
TEST_CONTROL_DATA_DICT = [{"name":"value","value":TEST_CONTROL_VALUE_VAL},
                          {"name":"color","value":TEST_CONTROL_COLOR_VAL}]


TEST_SERVICE_NAME = "test_service"
TEST_SERVICE_NAME2 = "test_service"

class TestControl():
    def test_no_data_or_callback(self):
        control = Control(name=TEST_CONTROL_NAME,
                          parent="hue",
                          desc="this is a control to turn on light",
                          action="turn on")
        output = control.clean_dict()

        assert "name" in output
        assert "parent" in output
        assert "description" in output
        assert "action" in output
        assert len(output["dataset"]) == 0
        assert output["name"] == TEST_CONTROL_NAME

    def test_data_set(self):
        control = Control(name=TEST_CONTROL_NAME,
                          parent="hue",
                          desc="this is a control to turn on light",
                          action="turn on",
                          dataset=TEST_CONTROL_DATASET)
        output = control.clean_dict()

        assert "name" in output
        assert "parent" in output
        assert "description" in output
        assert "action" in output
        assert len(output["dataset"]) == 2
        for data in output["dataset"]:
            assert data["name"] in TEST_CONTROL_DATASET
            assert data["type"] == TEST_CONTROL_DATASET[data["name"]]["type"]
            assert data["description"] == TEST_CONTROL_DATASET[data["name"]]["desc"]

    def test_no_callback(self):

        def callback(value, color):
            assert False

        control = Control(name=TEST_CONTROL_NAME,
                          parent="hue",
                          desc="this is a control to turn on light",
                          action="turn on",
                          dataset=TEST_CONTROL_DATASET)
        control.call()

    def test_callback_no_data(self):
        def callback():
            global run
            run = True

        control = Control(name=TEST_CONTROL_NAME,
                          parent="hue",
                          desc="this is a control to turn on light",
                          action="turn on",
                          dataset=TEST_CONTROL_DATASET,
                          callback=callback)
        control.call()
        assert run

    def test_callback(self):
        global run
        run = False
        def callback(value, color):
            global run
            run = True
            assert value == TEST_CONTROL_VALUE_VAL
            assert color == TEST_CONTROL_COLOR_VAL

        control = Control(name=TEST_CONTROL_NAME,
                          parent="hue",
                          desc="this is a control to turn on light",
                          action="turn on",
                          dataset=TEST_CONTROL_DATASET,
                          callback=callback)
        control.call(TEST_CONTROL_DATA_DICT)
        assert run



class TestElement():
    def test_no_data(self):
        element = Element(name=TEST_ELEMENT_NAME, parent="Hue")
        output = element.clean_dict()

        assert "name" in output
        assert "parent" in output
        assert "data" in output
        assert "controls" in output
        assert len(output["controls"]) == 0
        assert len(output["data"]) == 0
        assert output["name"] == TEST_ELEMENT_NAME

    def test_data(self):
        element = Element(name=TEST_ELEMENT_NAME, parent="Hue", data=TEST_ELEMENT_DATA)
        output = element.clean_dict()

        assert "name" in output
        assert "parent" in output
        assert "data" in output
        assert "controls" in output
        assert len(output["controls"]) == 0
        assert len(output["data"]) == 2

        for data in output["data"]:
            assert data["name"] in TEST_ELEMENT_DATA
            assert data["value"] == TEST_ELEMENT_DATA[data["name"]]

    def test_single_control(self):
        control = Control(name=TEST_CONTROL_NAME,
                          parent="hue",
                          desc="this is a control to turn on light",
                          action="turn on",
                          dataset=TEST_CONTROL_DATASET)
        element = Element(name=TEST_ELEMENT_NAME, parent="Hue", data=TEST_ELEMENT_DATA, controls=[control])
        output = element.clean_dict()

        assert "name" in output
        assert "parent" in output
        assert "data" in output
        assert "controls" in output
        assert len(output["controls"]) == 1
        assert len(output["data"]) == 2

    def test_multiple_controls(self):
        control = Control(name=TEST_CONTROL_NAME,
                          parent="hue",
                          desc="this is a control to turn on light",
                          action="turn on",
                          dataset=TEST_CONTROL_DATASET)
        control2 = Control(name=TEST_CONTROL_NAME + "2",
                          parent="hue",
                          desc="this is a control to turn on light",
                          action="turn on",
                          dataset=TEST_CONTROL_DATASET)
        element = Element(name=TEST_ELEMENT_NAME, parent="Hue", data=TEST_ELEMENT_DATA, controls=[control, control2])
        output = element.clean_dict()

        assert "name" in output
        assert "parent" in output
        assert "data" in output
        assert "controls" in output
        assert len(output["controls"]) == 2
        assert len(output["data"]) == 2

    def test_register_controls(self):
        control = Control(name=TEST_CONTROL_NAME,
                          parent="hue",
                          desc="this is a control to turn on light",
                          action="turn on",
                          dataset=TEST_CONTROL_DATASET)
        element = Element(name=TEST_ELEMENT_NAME, parent="Hue", data=TEST_ELEMENT_DATA)
        element.register_control(control)
        output = element.clean_dict()

        assert "name" in output
        assert "parent" in output
        assert "data" in output
        assert "controls" in output
        assert len(output["controls"]) == 1
        assert len(output["data"]) == 2

    def test_control_by_id(self):
        control = Control(name=TEST_CONTROL_NAME,
                          parent="hue",
                          desc="this is a control to turn on light",
                          action="turn on",
                          dataset=TEST_CONTROL_DATASET)
        control2 = Control(name=TEST_CONTROL_NAME + "2",
                          parent="hue",
                          desc="this is a control to turn on light",
                          action="turn on",
                          dataset=TEST_CONTROL_DATASET)
        element = Element(name=TEST_ELEMENT_NAME, parent="Hue", data=TEST_ELEMENT_DATA, controls=[control, control2])

        output = element.get_control_using_id(TEST_CONTROL_NAME)
        output = output.clean_dict()

        assert "name" in output
        assert "parent" in output
        assert "description" in output
        assert "action" in output
        assert len(output["dataset"]) == 2

class TestService():

    def test_no_attributes(self):
        service = Service(name = TEST_SERVICE_NAME)

    def test_single_element(self):
        element = Element(name=TEST_ELEMENT_NAME, parent="Hue", data=TEST_ELEMENT_DATA)
        service = Service(name = TEST_SERVICE_NAME, elements=[element])

        output = service.clean_dict()
        assert "name" in output
        assert output["name"] is TEST_SERVICE_NAME
        assert "id" in output
        assert output["id"] is TEST_SERVICE_NAME
        assert "elements" in output
        assert len(output["elements"]) == 1

    def test_multiple_elements(self):
        element = Element(name=TEST_ELEMENT_NAME, parent="Hue", data=TEST_ELEMENT_DATA)
        element2 = Element(name=TEST_ELEMENT_NAME+"2", parent="Hue", data=TEST_ELEMENT_DATA)
        service = Service(name = TEST_SERVICE_NAME, elements=[element, element2])

        output = service.clean_dict()
        assert "name" in output
        assert output["name"] is TEST_SERVICE_NAME
        assert "id" in output
        assert output["id"] is TEST_SERVICE_NAME
        assert "elements" in output
        assert len(output["elements"]) == 2

    def test_register_element(self):
        element = Element(name=TEST_ELEMENT_NAME, parent="Hue", data=TEST_ELEMENT_DATA)
        service = Service(name = TEST_SERVICE_NAME)
        service.register_element(element)

        output = service.clean_dict()
        assert "name" in output
        assert output["name"] is TEST_SERVICE_NAME
        assert "id" in output
        assert output["id"] is TEST_SERVICE_NAME
        assert "elements" in output
        assert len(output["elements"]) == 1


    def test_element_by_id(self):
        element = Element(name=TEST_ELEMENT_NAME, parent="Hue", data=TEST_ELEMENT_DATA)
        element2 = Element(name=TEST_ELEMENT_NAME+"2", parent="Hue", data=TEST_ELEMENT_DATA)
        service = Service(name = TEST_SERVICE_NAME, elements=[element, element2])

        output = service.get_element_using_id(TEST_ELEMENT_NAME)
        output = output.clean_dict()

        assert "name" in output
        assert "parent" in output
        assert "data" in output
        assert len(output["data"]) == 2


    def test_complete_service(self):
        element = Element(name=TEST_ELEMENT_NAME, parent="Hue", data=TEST_ELEMENT_DATA)
        service = Service(name = TEST_SERVICE_NAME, elements=[element])

        output = service.clean_dict()

        assert len(output["elements"]) == 1

    def test_merge(self):
        pytest.skip()

class TestStore():

    def test_no_service(self):
        store = Store()
        assert len(store.clean_dict()) is 0

    def test_register_method_one_service(self):
        store = Store()
        service = Service(name = TEST_SERVICE_NAME)
        store.register_service(service)

    def test_dict_one_service(self):
        store = Store()
        service = Service(name = TEST_SERVICE_NAME)
        store.register_service(service)

        output = store.clean_dict()

        assert "name" in output[0]
        assert output[0]["name"] is TEST_SERVICE_NAME
        assert "id" in output[0]
        assert output[0]["id"] is TEST_SERVICE_NAME
        assert "elements" in output[0]

    def test_get_id_one_service(self):
        store = Store()
        service = Service(name = TEST_SERVICE_NAME)
        store.register_service(service)

        service = store.get_service_using_id(TEST_SERVICE_NAME)
        output = service.clean_dict()

        assert "name" in output
        assert output["name"] is TEST_SERVICE_NAME
        assert "id" in output
        assert output["id"] is TEST_SERVICE_NAME
        assert "elements" in output

    def test_dict_many_service(self):
        store = Store()
        service = Service(name = TEST_SERVICE_NAME)
        service2 = Service(name = TEST_SERVICE_NAME2)
        store.register_service(service)
        store.register_service(service2)

        output = store.clean_dict()

        assert len(output) == 2

    def test_get_id_many_service(self):
        store = Store()
        service = Service(name = TEST_SERVICE_NAME)
        service2 = Service(name = TEST_SERVICE_NAME2)
        store.register_service(service)
        store.register_service(service2)

        service = store.get_service_using_id(TEST_SERVICE_NAME)
        output = service.clean_dict()

        assert "name" in output
        assert output["name"] is TEST_SERVICE_NAME
        assert "id" in output
        assert output["id"] is TEST_SERVICE_NAME
        assert "elements" in output

        service = store.get_service_using_id(TEST_SERVICE_NAME2)
        output = service.clean_dict()

        assert "name" in output
        assert output["name"] is TEST_SERVICE_NAME2
        assert "id" in output
        assert output["id"] is TEST_SERVICE_NAME2
        assert "elements" in output

    def test_merge_services(self):
        pytest.skip("apples")