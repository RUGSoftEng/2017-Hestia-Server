from abc import abstractmethod

import requests
from flask import json

from models.Device import Device
from plugins.philips.searching.LastSearch import LastSearch
from plugins.philips.searching.ReachableSearch import ReachableSearch


class PhilipsDevice(Device):

    def __init__(self, database, device_id):
        super().__init__(database, device_id)

    @classmethod
    @abstractmethod
    def setup(cls, required_info):
        pass

    @classmethod
    @abstractmethod
    def _get_lamp_id(cls, required_info, types):
        url = "http://" + required_info["ip"] + "/api" + required_info["user"] + "/lights"
        response = json.loads(requests.get(url).content)
        if required_info["search_method"] == "reachable":
            return ReachableSearch.search(response, types)
        elif required_info["search_method"] == "last":
            return LastSearch.search(response, types)

    @classmethod
    def _get_new_user(cls, required_info, ):
        """ 
        Philips hue needs a string as identification for communication. When no
        string is given or it is said to be unknown this method retrieves a
        string that can be used as identification for all further communications
        . It also adds the id of this device to the required_info, using this
        the activator can remove the device when needed.
        """
        if required_info["user"] in ["unknown", ""]:
            data = '{"devicetype":"hue#' + required_info["plugin"] + '"}'
            response = requests.post("http://" + required_info["ip"]
                                     + "/api", data)
            message = json.loads(response.content)[0]
            success = message["success"]

            return success["username"]

        else:
            return required_info["user"]
