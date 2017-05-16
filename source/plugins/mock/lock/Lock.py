from models.Device import Device


class Lock(Device):
    """"
    Mock lock device. 
    """

    @classmethod
    def setup(cls, required_info):
        print("Mock lock is being setup")
        return required_info
