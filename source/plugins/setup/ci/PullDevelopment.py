import os
from git import Repo


from model.Activator import Activator
from model.util.stringToBool import string_to_bool


class PullDevelopment(Activator):
    def __init__(self):
        super().__init__()
        self._state = False

    @property
    def state(self):
        return self._state

    @property
    def type(self):
        return "bool"

    def perform(self, devicerequired_info):
        """
        First changes the app debug mode and then pulls development.
        """
        # Import is only be able to made here otherwise server crashes
        # at startup due to circular imports
        from application import app

        ci_path = os.path.dirname(os.path.abspath(__file__))
        app_path = os.path.dirname(os.path.dirname(os.path.dirname(ci_path)))
        server_path = os.path.dirname(app_path)
        old_debug = app.debug
        app.debug = True
        repo = Repo(server_path)
        git = repo.git
        git.checkout("development")
        git.pull()
        app.debug = old_debug

    def set_state_with_string(self, value):
        self._state = string_to_bool(value)

    @property
    def name(self):
        return "Pull development"
