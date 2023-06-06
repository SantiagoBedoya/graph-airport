from tkinter import Tk
from models.airport import Airport
from graph.graph import Graph
from components.drawer import Drawer


class App(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Graph Airport")
        self.minsize(width=1000, height=800)

        a = Airport(200, 10, "a", "0")
        b = Airport(600, 80, "b", "0")
        c = Airport(10, 150, "c", "0")
        d = Airport(600, 220, "d", "0")
        e = Airport(10, 290, "e", "0")
        f = Airport(600, 360, "f", "0")
        g = Airport(10, 430, "g", "0")

        self.graph = Graph()
        self.graph.add_node(a, [b, c])
        self.graph.add_node(b, [a, d])
        self.graph.add_node(c, [a, d, f])
        self.graph.add_node(d, [e])
        self.graph.add_node(e, [f])
        self.graph.add_node(f, [g])
        self.graph.add_node(g, [])

        self.drawer = Drawer(self)
        self.render()

    def render(self):
        for airport, connections in self.graph.data.items():
            self.drawer.draw_airport(airport)

            for connection in connections:
                self.drawer.draw_route(airport, connection)


if __name__ == "__main__":
    app = App()
    app.mainloop()
