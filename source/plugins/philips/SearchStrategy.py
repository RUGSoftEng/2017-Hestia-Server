from abc import ABC, abstractmethod


class SearchStrategy(ABC):
    """
    Classes implementing this abstract classes are used for searching the lamp_id.
    """
    @classmethod
    @abstractmethod
    def search(cls, response, types):
        pass
