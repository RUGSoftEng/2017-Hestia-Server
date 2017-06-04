import datetime

import jwt as jwt


class LoginLogic:
    def __init__(self, user_database):
        self._user_database = user_database

    def login_user(self, username, password):
        user = self._user_database.get_user(username)
        if user.validate_password(password):
            return self.encode_auth_token(username)

    def encode_auth_token(self, username):
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7, seconds=0),
            'user': username
        }
        return jwt.encode(
            payload,
            'BullShitKey',
            algorithm='HS256'
        )
