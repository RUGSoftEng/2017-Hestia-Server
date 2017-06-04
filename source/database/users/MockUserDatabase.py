from database.users.UserDatabase import UserDatabase
from models.User import User


class MockUserDatabase(UserDatabase):
    def get_user(self, user_id_or_name):
        return User("test", "wachtwoord")

    def add_user(self, user):
        pass