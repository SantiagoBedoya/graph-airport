import networkx as nx
import matplotlib.pyplot as plt
from ..graph.node import Node
from ..models.airport import Airport


class Graph:
    def __init__(self) -> None:
        self.g = nx.Graph()
        self.nodes = {} # {1: (0, 0), 2: (-1, 0.3), 3: (2, 0.17), 4: (4, 0.255), 5: (5, 0.03)}


    def add_node(self, node: Node, coords):
        self.nodes[node] = (coords[0], coords[1])

    def add_edge(self, start: str, end: str):
        self.g.add_edge(start, end)

    def render(self) -> None:
        nx.draw_networkx(
            self.g,
            self.nodes,
            {
                "font_size": 36,
                "node_size": 3000,
                "node_color": "white",
                "edgecolors": "black",
                "linewidths": 5,
                "width": 5,
            },
        )
        ax = plt.gca()
        ax.margins(0.20)
        plt.axis("off")
        plt.show()
        
