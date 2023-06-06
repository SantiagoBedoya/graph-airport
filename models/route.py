from .airport import Airport
from graph.edge import Edge

class Route(Edge):
    def __init__(self, origin: Airport, destination: Airport, distance: int, time: int) -> None:
        super().__init__(origin, destination, distance)
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.time = time