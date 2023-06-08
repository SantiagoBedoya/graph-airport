
<<<<<<< HEAD

class Airport(Node):
    def __init__(self, x:int, y:int, name:str, code:str) -> None:
        super().__init__(x, y)
=======
class Airport:
    def __init__(self, x: int, y: int, name: str, code: str) -> None:
        self.x = x
        self.y = y
>>>>>>> main
        self.name = name
        self.code = code
