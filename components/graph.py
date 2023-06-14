import networkx as nx
import matplotlib.pyplot as plt
from models.airport import Airport
from models.route import Route

class Graph:
    def __init__(self, airports:list[Airport], routes: list[Route]) -> None:
        self.g = nx.Graph()
        self.nodes = {}

        self.airports_to_nodes(airports)
        self.routes_to_edges(routes)

    def add_node(self, node, coords):
        self.g.add_node(node)
        self.nodes[node] = (coords[0], coords[1])

    def add_edge(self, start: str, end: str, weight: int, time: int):
        self.g.add_edge(start, end, weight=weight, time=time)

    def airports_to_nodes(self, airports: list[Airport]):
        for airport in airports:
            self.add_node(airport.code, (airport.x, airport.y))
    
    def routes_to_edges(self, routes: list[Route]):
        for route in routes:
            self.add_edge(route.start.code, route.end.code, route.distance, route.time)

    def search(self, from_airport: Airport, to_airport: Airport, search_by: int = 1):
        sby = "weight"
        if search_by == 2:
            sby = "time"
        result = nx.dijkstra_path(self.g, from_airport.code, to_airport.code, weight=sby)
        return result

    def render(self) -> None:
        nx.draw_networkx_nodes(self.g, self.nodes, node_color="yellow")
        nx.draw_networkx_edges(self.g, self.nodes, edge_color="gray")
        nx.draw_networkx_labels(self.g, self.nodes)
        nx.draw_networkx_edge_labels(self.g, self.nodes, edge_labels={(u, v): f"{d['weight']}km - {d['time']}min" for u, v, d in self.g.edges(data=True)})
        ax = plt.gca()
        ax.margins(0.20)
        plt.axis("off")
        plt.show()
        
