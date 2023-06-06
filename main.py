from tkinter import Tk
from models.airport import Airport
from graph.graph import Graph
from components.drawer import Drawer

class App(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Graph Airport")
        self.minsize(width=1000, height=650)

        a = Airport(10, 10, "a")
        b = Airport(600, 80, "b")
        c = Airport(10, 150, "c")
        d = Airport(600, 220, "d")
        e = Airport(10, 290, "e")
        f = Airport(600, 360, "f")
        g = Airport(10, 430, "g")

        self.graph = Graph()
        self.graph.add_node(a, [b, c])
        self.graph.add_node(b, [a, d])
        self.graph.add_node(c, [a, d, f])
        self.graph.add_node(d, [e])
        self.graph.add_node(e, [f])
        self.graph.add_node(f, [g])
        self.graph.add_node(g, [])

        self.drawer = Drawer(self, 700, 500, 300, 0)
        self.render()

    def render(self):
        for airport, connections in self.graph.data.items():
            self.drawer.draw_airport(airport)

            for connection in connections:
                self.drawer.draw_route(airport, connection)

if __name__ == '__main__':
    app = App()
    app.mainloop()
