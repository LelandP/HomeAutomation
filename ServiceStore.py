import plugins
import importlib

class Store(object):
    """
    """
    def __init__(self):
        """
        """
        self.services = []

        module_list = plugins.get_all_plugins()
        for module in module_list:
            i = importlib.import_module("plugins." + module)
            self.register_service(i.init_service_class())

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
    def __init__(self, name, controls=None, elements=None):
        """
        """
        self.id = name
        self.name = self.id
        self.controls = []
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
                    elements=[e.clean_dict() for e in self.elements],
                    controls=[c.clean_dict() for c in self.controls])

class Element(object):
    """
    """
    def __init__(self, name, parent, data=None):
        """
        """
        self.id = name
        self.name = self.id
        self.parent = parent
        if data is not None:
            self.data = data
        else:
            self.data = {}

    def clean_dict(self):
        """
        """
        data = []
        for key, value in self.data.iteritems():
            data.append({"name": key, "value": value})
        return dict(id=self.id, name=self.name, parent=self.parent,
                    data=data)