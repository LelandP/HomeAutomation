import json
from ServiceStore import Store
from ResponseFormatter import add_href_to_list, filter_dict
from flask import request

#TO-DO: load this better
store = Store()

#TO-DO: filter elements based on swagger

def get_services():
    """
    """
    #filter_dict exclude=["controls", "elements"]
    return [filter_dict(s, exclude=["controls", "elements"]) for s in add_href_to_list(request.url, store.clean_dict())]

def get_service(serviceid):
    """
    """
    service = store.get_service_using_id(serviceid)
    #TO-DO: return 404 if it dosent exist
    updated_dict = service.clean_dict()
    updated_dict.update({"controls": request.url + "/controls",
                         "elements": request.url + "/elements"})
    return updated_dict

def get_controls(serviceid):
    """
    """
    service = store.get_service_using_id(serviceid)
    #TO-DO: return 404 if it dosent exist
    return '{}'

def get_control(serviceid, controlid):
    """
    """
    return '{}'

def get_elements(serviceid):
    """
    """
    service = store.get_service_using_id(serviceid)
    return [filter_dict(e, exclude=["data", "parent"]) for e in add_href_to_list(request.url, service.clean_dict()["elements"])]

def get_element(serviceid, elementid):
    """
    """
    service = store.get_service_using_id(serviceid)
    element = service.get_element_using_id(elementid)
    return element.clean_dict()


