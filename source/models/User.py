class User:
    def __init__(self, username, password, rights, devices):
        self._username = username
        self._password = password
        self._rights = rights
        self._devices = devices

    def validate_password(self, password):
        return True

    def get_rights(self):
        return ["admin"]

    def get_device_ids(self):
        return ["000"]
