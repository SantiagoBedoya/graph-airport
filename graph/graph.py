from .node import Node
from .edge import Edge

class Graph:
    def __init__(self) -> None:
        self.data = {}

    def add_node(self, node: Node):
        self.data[node] = []

    def add_edge_to_node(self, node: Node, edge: Edge):
        self.data[node].append(edge)

    def get_nodes(self) -> list[Node]:
        return self.data.keys()

    def get_edges_of_node(self, node: Node) -> list[Edge]:
        return self.data[node]