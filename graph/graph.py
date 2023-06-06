from .node import Node

class Graph:
    def __init__(self) -> None:
        self.data = {}

    def add_node(self, node: Node, connections: list[Node]):
        self.data[node] = connections