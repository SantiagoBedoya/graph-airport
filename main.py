from tkinter import Tk
from models.airport import Airport
from components.drawer import Drawer


class App(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Graph Airport")
        self.minsize(width=1000, height=800)

        a = Airport(200, 10, "a")
        b = Airport(600, 80, "b")
        c = Airport(10, 150, "c")
        d = Airport(600, 220, "d")
        e = Airport(10, 290, "e")
        f = Airport(600, 360, "f")
        g = Airport(10, 430, "g")
        self.graph = {
            a: [b, c],
            b: [a, d],
            c: [a, d, f],
            d: [e],
            e: [f],
            f: [g],
            g: [a],
        }

        self.drawer = Drawer(self, 0.7, 1, 300, 10)
        self.render()

    def render(self):
        for airport, connections in self.graph.items():
            print(f"drawing airport {airport.name}, connections: {len(connections)}")
            self.drawer.draw_airport(airport)

            for connection in connections:
                self.drawer.draw_route(airport, connection)


if __name__ == "__main__":
    app = App()
    app.mainloop()
