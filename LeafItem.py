# from typing import override

from ComponentBag import ComponentBag


class LeafItem(ComponentBag):

    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    # @override
    def add_item(self, item):
        pass

    # @override
    def remove_item(self, item):
        pass

    # @override
    def get_items(self):
        return None

    # @override
    def get_weight(self):
        return self.weight

    def __str__(self):
        return f"{self.name} {self.weight}"
