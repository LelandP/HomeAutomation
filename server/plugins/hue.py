from ServiceStore import Service, Element, Control
from phue import Bridge
import os

#192.168.0.100
#TO-DO: get address from 
#TO-DO: use contexts to the bridge, or some type of servie storage
HUE_ADDRESS = os.getenv("HUE_ADDRESS", None)
if HUE_ADDRESS == None:
    print "Hue bridge ip not set, use HUE_ADDRESS"
    exit()
bridge = Bridge(HUE_ADDRESS)
bridge.connect()

def turn_light_on_off(light_name, state):
    bridge.set_light(light_name, "on", s in ['true', '1', 't', 'True'])

def init_service_class():
    """
    """
    lighting = Service("Lighting")

    #get the whole api dict
    #you only want to do this once.. trust me
    api = bridge.get_api()
    for index, light in api["lights"].iteritems():
        print light
        data_dict = {"on":str(light["state"]["on"]),
                     "bri":str(light["state"]["bri"])}
        light_element = Element(light["name"], "Hue", data=data_dict)

        toggle_state_control = Control(name="toggleState",
                                       parent="Hue",
                                       desc="Will toggle state on state of the light",
                                       action="On/Off",
                                       callback=(lambda value: turn_light_on_off(light_name=light["name"], state=value)),
                                       dataset={"value":{"desc":"Value of the on state.(True:on, False:off)", "type":"bool"}})
        light_element.register_control(toggle_state_control)

        lighting.register_element(light_element)

    return lighting



    #TO-DO: get ip from upnp

    # if HUE_ADDRESS == None:
    #     print "Hue bridge ip not set, use HUE_ADDRESS"
    #     return None

    # bridge = Bridge(HUE_ADDRESS)
    # bridge.connect()

    # is_on = bridge.get_light('bed left', 'on')
    # print is_on
    # if is_on:
    #     bridge.set_light('bed left', "on", False)
    # else:
    #     bridge.set_light('bed left', "on", True)

    # exit()


# print b.get_api()
# b.set_light( [1,2], 'on', True)
