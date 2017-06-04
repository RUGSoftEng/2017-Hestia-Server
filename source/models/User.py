class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def validate_password(self, password):
        return True

    def generate_token(self):
        return "SomeBullShitToken"
