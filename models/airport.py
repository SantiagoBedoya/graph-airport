from graph.node import Node


class Airport(Node):
    def __init__(self, x:int, y:int, name:str, code:str) -> None:
        super().__init__(x, y)
        self.name = name
        self.code = code
