import requests
from flask import json


def send_state_change_to_bridge(ip, user, lamp_id, data):
    url = ("http://" + ip
           + "/api/" + user
           + "/lights/" + str(lamp_id)
           + "/state")
    return requests.put(url, data)


def get_new_user_if_needed(required_info):
    """
    Philips hue needs a string as identification for communication. When no
    string is given or it is said to be unknown this method retrieves a
    string that can be used as identification for all further communications
    . It also adds the id of this device to the required_info, using this
    the activator can remove the device when needed.
    """
    if is_user_unknown(required_info):
        get_new_user(required_info)


def is_user_unknown(required_info):
    given_user = required_info["user"]
    possible_users = ["unknown", ""]
    return given_user in possible_users


def get_new_user(required_info):
    data = '{"devicetype":"hue#'+required_info["plugin"]+'"}'
    response = requests.post("http://" + required_info["ip"]
                             + "/api", data)
    message = json.loads(response.content)[0]
    success = message["success"]
    required_info["user"] = success["username"]


def get_lamp_id_for_types(required_info, types):
    """
             Gets the id of the new lamp. Can use two different methods.
             last :         retrieves the id of the last lamp added to the philips
                            hue bridge.
             reachable :    retrieves the id of the only lamp that is currently
                            reachable. This requires all other lights not to have
                            power.
             """
    url = "http://" + required_info["ip"] + "/api" + required_info["user"] + "/lights"
    response = json.loads(requests.get(url).content)
    if required_info["search_method"] == "reachable":
        lamp_id = reachable_search_method(response, types)

    elif required_info["search_method"] == "last":
        lamp_id = last_search_method(response, types)

    required_info["lamp_id"] = lamp_id


def reachable_search_method(response, types):
    found = False
    for key, value in response.items():
        if value['state']['reachable'] and value['type'] in types:
            if found:
                raise Exception("Multiple lights were found")
            else:
                found = True
                lamp_id = int(key)

    if not found:
        raise Exception("No lights were found")

    return lamp_id


def last_search_method(response, types):
    found = False
    for key, value in response.items():
        if value['state'] and value['type'] in types:
            found = True
            lamp_id = int(key)

    if not found:
        raise Exception("No lights were found")

    return lamp_id
