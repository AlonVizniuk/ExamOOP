from abc import ABC, abstractmethod


class Giftable(ABC):

    @abstractmethod
    def open_gift(self):
        pass