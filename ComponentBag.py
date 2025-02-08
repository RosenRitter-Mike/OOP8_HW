from abc import ABC, abstractmethod


class ComponentBag(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def remove_item(self, item):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_weight(self):
        pass
