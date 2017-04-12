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
        import os
        from git import Repo
        from application import app
        ci_path = os.path.abspath(__file__)
        app_path = os.path.dirname(os.path.dirname(os.path.dirname(ci_path)))
        server_path = os.path.dirname(app_path)
        debug = app.debug
        app.debug = True
        repo = Repo(server_path)
        git = repo.git
        git.checkout("feature/hestia_ci'")
        git.pull()
        app.debug = debug

    def set_state_with_string(self, value):
        self._state = string_to_bool(value)

    @property
    def name(self):
        return "Pull development"
