from abc import ABC, abstractmethod


class SearchStrategy(ABC):
    @classmethod
    @abstractmethod
    def search(cls, response, types):
        pass
