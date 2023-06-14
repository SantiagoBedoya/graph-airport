import networkx as nx
import matplotlib.pyplot as plt
from models.airport import Airport
from models.route import Route

class Graph:
    """Graph
    
    This class contains all the necessary methods so that the graph can be displayed.

    Args:
        airports (list[Airport]): list of airports to be displayed in the graph
        routes (list[Route]): List of routes that are connected between the airports
    """
    def __init__(self, airports:list[Airport], routes: list[Route]) -> None:
        self.g = nx.Graph()
        self.nodes = {}

        self.airports_to_nodes(airports)
        self.routes_to_edges(routes)

    def add_node(self, node, coords):
        """Add node
        
        This method is responsible for adding a node to the graph

        Args:
            node (Node): node to add to the graph
            coords (list[float]): coordinates where the node will be located
        """
        self.g.add_node(node)
        self.nodes[node] = (coords[0], coords[1])

    def add_edge(self, start: str, end: str, weight: int, time: int):
        """Add edge
        
        This method is responsible for displaying the line that connects two nodes

        Args
            start (str): Airport code where the route begins
            end (str): Airport code where the route ends
            weight (int): line thickness
            time(int): time it takes to travel between airports
        """
        self.g.add_edge(start, end, weight=weight, time=time)

    def airports_to_nodes(self, airports: list[Airport]):
        """Airports to nodes 
        
        This method transforms airports to nodes to plot them on the graph

        Args:
            airports (list[Airport]): List of airports to be plotted
        """
        for airport in airports:
            self.add_node(airport.code, (airport.x, airport.y))
    
    def routes_to_edges(self, routes: list[Route]):
        """Routes to edges
        
        This method converts the routes into lines to connect the airports

        Args:
            routes (list[Route]): List of routes to be plotted as lines
        """
        for route in routes:
            self.add_edge(route.start.code, route.end.code, route.distance, route.time)

    def search(self, from_airport: Airport, to_airport: Airport, search_by: int = 1):
        """Search routes

        This method uses the Dijkstra methodology to define which is the best route, either by time or by distance.
        
        Args:
            from_aiport (Airport): departure airport
            to_airport (Airport): arrival airport
            search_by (int): if you search by distance the indicator will be 1, but if you search by time the indicator will be 2
        """
        sby = "weight"
        if search_by == 2:
            sby = "time"
        result = nx.dijkstra_path(self.g, from_airport.code, to_airport.code, weight=sby)
        return result

    def remove_edge(self, start: Airport, end:Airport):
        """Remove edge
        
        This method is responsible for eliminating an edge

        Args:
            start (Airport): departure airport
            end (Airport): arrival airport
        """
        self.g.remove_edge(start.code, end.code)

    def render(self) -> None:
        """Render
        
        This method is responsible for rendering the components of the class
        """
        nx.draw_networkx_nodes(self.g, self.nodes, node_color="yellow")
        nx.draw_networkx_edges(self.g, self.nodes, edge_color="gray")
        nx.draw_networkx_labels(self.g, self.nodes)
        nx.draw_networkx_edge_labels(self.g, self.nodes, edge_labels={(u, v): f"{d['weight']}km - {d['time']}min" for u, v, d in self.g.edges(data=True)})
        ax = plt.gca()
        ax.margins(0.20)
        plt.axis("off")
        plt.show()
        
