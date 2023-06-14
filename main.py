from tkinter import Tk
from components.graph import Graph
from components.airport_form import AirportForm
from components.route_form import RouteForm
from components.graph_button import GraphButton
from components.search_button import SearchButton
from components.search_form import SearchForm
from models.airport import Airport
from models.route import Route


class App(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Graph Airport")
        self.minsize(width=800, height=400)
        self.maxsize(width=800, height=400)

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
        # self.graph_button = GraphButton(self, self.show_graph)
        self.search_button = SearchButton(self, self.show_search_form)

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

    def show_search_form(self):
        SearchForm(self, self.find_airport_by_code, self.search)
        pass

    def search(self, from_airport: Airport, to_airport: Airport, search_by: int):
        self.graph.search(from_airport, to_airport, search_by)
        pass



if __name__ == "__main__":
    app = App()
    app.mainloop()
