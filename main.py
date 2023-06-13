from tkinter import Tk
from components.graph import Graph
from components.airport_form import AirportForm
from components.route_form import RouteForm
from components.graph_button import GraphButton
from models.airport import Airport
from models.route import Route


class App(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Graph Airport")
        self.minsize(width=350, height=650)

        airport1 = Airport(10, 10, "Airport 1", "001")
        airport2 = Airport(15, 15, "Airport 2", "002")
        airport3 = Airport(0, 0, "Airport 3", "003")
        self.airports = [
            airport1,
            airport2,
            airport3,
        ]

        
        self.routes = [
            Route(airport1, airport2, 200, 30),
            Route(airport1, airport3, 1000, 120),
        ]

        self.graph = Graph(self.airports, self.routes)
        self.airport_form = AirportForm(self, self.airports, self.save_airport)
        self.route_form = RouteForm(self, self.routes, self.save_route, self.find_airport_by_code)
        self.graph_button = GraphButton(self, self.show_graph)

        self.render()

    def find_airport_by_code(self, code: str):
        for airport in self.airports:
            if airport.code == code:
                return airport
            
        return None

    def save_airport(self, name: str, code: str, coord_x: int, coord_y: int):
        self.graph.add_node(code, (coord_x, coord_y))

    def save_route(self, start, end, distance, time):
        self.graph.add_edge(start, end, distance, time)

    def show_graph(self):
        self.graph.render()

    def init_components(self):
        self.airport_form.render()
        # self.route_form.render()

        self.graph_button.render()

    def render(self):
        self.init_components()


if __name__ == "__main__":
    app = App()
    app.mainloop()
