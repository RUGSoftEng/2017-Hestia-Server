from abc import ABC, abstractmethod


class UserDatabase(ABC):
    @abstractmethod
    def get_user(self, user_id_or_name):
        pass

    @abstractmethod
    def add_user(self, user):
        pass