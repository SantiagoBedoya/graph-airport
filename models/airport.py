
class Airport:
    """Airport
    
    This class contains the attributes of an airport

    Args: 
        x (float): x-coordinate
        y (float): y-coordinate
        name (str): airport name
        code (str): airport code
    """
    def __init__(self, x: float, y: float, name: str, code: str) -> None:
        self.x = x
        self.y = y
        self.name = name
        self.code = code
