from models.Activator import Activator


class LightDimmer(Activator):
    def perform(self, options):
        print("Configuration is set to: " + str(self.state))
