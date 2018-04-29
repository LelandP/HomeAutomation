import json
from ServiceStore import Store
from ResponseFormatter import add_href_to_list, filter_dict
from flask import request
import urllib

#TO-DO: load this better
store = Store()

#TO-DO: filter elements based on swagger

def get_services():
    """
    """
    #filter_dict exclude=["controls", "elements"]
    return [filter_dict(s, exclude=["elements"]) for s in add_href_to_list(request.url, store.clean_dict())]

def get_service(serviceid):
    """
    """
    service = store.get_service_using_id(serviceid)
    if service is None:
        return "Service Not Found", 404
    updated_dict = service.clean_dict()
    updated_dict.update({"elements": request.url + "/elements"})
    return updated_dict

def get_elements(serviceid):
    """
    """
    service = store.get_service_using_id(serviceid)
    if service is None:
        return "Service Not Found", 404
    return [filter_dict(e, exclude=["data", "parent", "controls"]) for e in add_href_to_list(request.url, service.clean_dict()["elements"])]

def get_element(serviceid, elementid):
    """
    """
    service = store.get_service_using_id(serviceid)
    if service is None:
        return "Service Not Found", 404
    element = service.get_element_using_id(urllib.unquote_plus(elementid))
    if element is None:
        return "Element Not Found", 404
    updated_dict = element.clean_dict()
    updated_dict.update({"controls": request.url + "/controls"})
    return updated_dict

def get_controls(serviceid, elementid):
    """
    """
    service = store.get_service_using_id(serviceid)
    if service is None:
        return "Service Not Found", 404
    element = service.get_element_using_id(urllib.unquote_plus(elementid))
    if element is None:
        return "Element Not Found", 404
    print element.clean_dict()
    return [filter_dict(e, exclude=["dataset", "parent", "action", "description"]) for e in add_href_to_list(request.url, element.clean_dict()["controls"])]

def get_control(serviceid, elementid, controlid):
    """
    """
    service = store.get_service_using_id(serviceid)
    if service is None:
        return "Service Not Found", 404
    element = service.get_element_using_id(urllib.unquote_plus(elementid))
    if element is None:
        return "Element Not Found", 404
    control = element.get_control_using_id(controlid)
    if control is None:
        return "Control Not Found", 404
    return control.clean_dict()
