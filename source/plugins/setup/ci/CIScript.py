import os

from git import Repo

ci_path = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.dirname(os.path.dirname(os.path.dirname(ci_path)))
server_path = os.path.dirname(app_path)
repo = Repo(server_path)
origin = repo.remotes.origin
git = repo.git
git.checkout("development")
git.pull()
print("reached")