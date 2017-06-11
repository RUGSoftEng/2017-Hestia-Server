from abc import ABC, abstractmethod


class HestiaException(Exception, ABC):

    @abstractmethod
    def to_dict(self):
        pass

    @abstractmethod
    def get_http_code(self):
        pass