from .airport import Airport

class Route:
    """Route
    
    This class contains the attributes that a route has.

    Args:
        start (Airport): departure airport
        end (Airport): arrive airport
        distance (float): distance between airports
        time (float):: time it takes from the departure airport to the arrival airport
    """
    def __init__(self, start: Airport, end: Airport, distance: float, time: float) -> None:
        self.start = start
        self.end = end
        self.distance = distance
        self.time = time