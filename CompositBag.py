# from typing import override

from ComponentBag import ComponentBag


class CompositeBag(ComponentBag):

    def __init__(self, name):
        super().__init__(name)
        self.items = []

    # @override
    def add_item(self, item):
        self.items.append(item)

    # @override
    def remove_item(self, item):
        self.items.remove(item)

    # @override
    def get_items(self):
        return self.items

    # @override
    def get_weight(self):
        return sum(item.get_weight() for item in self.items)
