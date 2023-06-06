from graph.node import Node


class Airport(Node):
    def __init__(self, x, y, name, code) -> None:
        super().__init__(x, y)
        self.name = name
        self.code = code
