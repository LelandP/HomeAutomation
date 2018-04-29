import plugins
import importlib

class Store(object):
    """
    """
    def __init__(self):
        """
        """
        #TO-DO: this id broken in the tests, we need to fix the plugin importing for tests
        self.services = []

        try:

            module_list = plugins.get_all_plugins()
            for module in module_list:
                i = importlib.import_module("plugins." + module)
                service = i.init_service_class()
                if service is not None:
                    self.register_service(service)

        except Exception as e:
            print "Failed to load plugin: {}".format(e.message)

    def register_service(self, service):
        """
        """
        #TO-DO: merge if the id exists
        self.services.append(service)

    def get_service_using_id(self, uniqueid):
        """
        """
        for service in self.services:
            if service.id == uniqueid:
                return service


    def clean_dict(self):
        """
        """
        return [s.clean_dict() for s in self.services]

class Service(object):
    """
    """
    def __init__(self, name, elements=None):
        """
        """
        self.id = name
        self.name = self.id
        self.elements = []

        if elements is not None:
            for element in elements:
                self.register_element(element)

    def register_element(self, element):
        """
        """
        #TO-DO: merge is alredy exists
        self.elements.append(element)

    def get_element_using_id(self, uniqueid):
        """
        """
        for element in self.elements:
            if element.id == uniqueid:
                return element

    def clean_dict(self):
        """
        """
        return dict(id=self.id, name=self.name,
                    elements=[e.clean_dict() for e in self.elements])

class Element(object):
    """
    """
    def __init__(self, name, parent, controls=None, data=None):
        """
        """
        self.id = name
        self.name = self.id
        self.controls = []
        self.parent = parent
        if data is not None:
            self.data = data
        else:
            self.data = {}

        if controls is not None:
            for control in controls:
                self.register_control(control)

    def register_control(self, control):
        """
        """
        #TO-DO: merge is alredy exists
        self.controls.append(control)

    def get_control_using_id(self, uniqueid):
        """
        """
        for control in self.controls:
            if control.id == uniqueid:
                return control

    def clean_dict(self):
        """
        """
        data = []
        for key, value in self.data.iteritems():
            data.append({"name": key, "value": value})
        return dict(id=self.id, name=self.name, parent=self.parent,
                    data=data, controls=[c.clean_dict() for c in self.controls])

class Control(object):
    """
    """
    def __init__(self, name, parent, desc, action, callback=None, dataset=None):
        """
        """
        self.id = name
        self.name = self.id
        self.parent = parent
        self.desc = desc
        self.action = action
        self.callback = callback
        if dataset is not None:
            self.dataset = dataset
        else:
            self.dataset = {}

    def call(self, data=None):
        """
        """
        if self.callback is None:
            return

        if data is None:
            data = []

        kwargs = {}
        for element in data:
            kwargs.update({element["name"]: element["value"]})

        self.callback(**kwargs)



    def clean_dict(self):
        """
        """
        dataset = []
        for key, value in self.dataset.iteritems():
            dataset.append({"name": key, "description": value["desc"], "type": value["type"]})
        return dict(id=self.id, name=self.name, parent=self.parent,
                    description=self.desc, action=self.action,
                    dataset=dataset)
        
