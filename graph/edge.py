from .node import Node

class Edge:
    def __init__(self, start: Node, end: Node, weight: int) -> None:
        self.start = start
        self.end = end
        self.weight = weight