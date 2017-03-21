class Action():
    cntr = 0

    def __init__(self, name, actionType):
        Action.cntr += 1
        self.actionId = Action.cntr
        self.name = name
        self.actionType = actionType
        self.state = 0.0

    def setState(self, value):
        if not isinstance(value, int):
            raise Exception()

        self.state = value
        if value == True:
            doNothing = value
            # do a
        else:
            doNothing = value
            # do b




