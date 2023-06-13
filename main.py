from tkinter import Tk
from components.graph import Graph
from components.airport_form import AirportForm
from components.route_form import RouteForm
from components.graph_button import GraphButton


class App(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Graph Airport")
        self.minsize(width=350, height=650)
        

        self.graph = Graph()
        self.airport_form = AirportForm(self)
        self.route_form = RouteForm(self)
        self.graph_button = GraphButton(self, self.show_graph)

        self.graph.add_node(1, (0, 0))
        self.graph.add_node(2, (1, 1))
        # self.graph.add_edge(1, 2)

        self.render()

    def show_graph(self):
        self.graph.render()
    
    def init_components(self):
        self.airport_form.render()
        self.route_form.render()

        self.graph_button.render()

    def render(self):
        self.init_components()


if __name__ == "__main__":
    app = App()
    app.mainloop()
