from models.Activator import Activator


class LightSwitch(Activator):

    def perform(self, options):
        if self.state:
            print("Turn light on")
        else:
            print("Turn light off")
