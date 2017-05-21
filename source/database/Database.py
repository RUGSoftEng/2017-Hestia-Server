from abc import ABC, abstractmethod


class Database(ABC):
    """
    This class communicates with the MongoDB database. 
    It has several methods for this communication.
    """

    @abstractmethod
    def get_all_devices(self):
        """Instantiates all devices in database"""
        pass

    @abstractmethod
    def get_device(self, device_id):
        """Instantiates the device with the given device_id"""
        pass

    @abstractmethod
    def add_device(self, plugin):
        """Adds the given plugin info as a new device"""
        pass

    @abstractmethod
    def delete_device(self, device_id):
        pass

    @abstractmethod
    def update_field(self, device_id, field, new_value):
        pass

    @abstractmethod
    def get_field(self, device_id, field):
        pass

    @abstractmethod
    def get_activator_field(self, device_id, activator_id, field):
        pass

    @abstractmethod
    def update_activator_field(self, device_id, activator_id, field, new_value):
        pass

    @abstractmethod
    def _get_class(module, class_name):
        pass
