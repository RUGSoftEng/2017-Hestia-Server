from models.Activator import Activator


class ActivateLock(Activator):
    """
    Activator for the mock lock plugin. Depicts how a lock could be
    closed or opened.
    """

    def perform(self, options):
        if self.state:
            print("Open lock")
        else:
            print("Close lock")
