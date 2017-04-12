import os

from git import Repo

from application import app

ci_path = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.dirname(os.path.dirname(os.path.dirname(ci_path)))
server_path = os.path.dirname(app_path)

debug = app.debug
app.debug = True

repo = Repo(server_path)
origin = repo.remotes.origin
git = repo.git
git.checkout("feature/hestia_ci'")
git.pull()

app.debug = debug;
