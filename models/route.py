from .airport import Airport
from graph.edge import Edge

class Route(Edge):
    def __init__(self, start: Airport, end: Airport, distance: int, time: int) -> None:
        super().__init__(start, end, distance)
        self.start = start
        self.end = end
        self.distance = distance
        self.time = time