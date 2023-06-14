from .airport import Airport

class Route:
    def __init__(self, start: Airport, end: Airport, distance: float, time: float) -> None:
        self.start = start
        self.end = end
        self.distance = distance
        self.time = time