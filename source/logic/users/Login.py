class LoginLogic:
    def __init__(self, user_database):
        self._user_database = user_database

    def login_user(self, username, password):
        user = self._user_database.get_user(username)
        if user.validate_password(password):
            return user.generate_token()
