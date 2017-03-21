class Device():
    cntr = 0

    def __init__(self, name):
        Device.cntr += 1
        self.deviceId = Device.cntr
        self.name = name
        self.actions = list()

    def get(self, actionId):
        return next(action for action in self.actions if action.actionId == actionId)

    def addAction(self, action):
        self.actions.append(action)


