from tkinter import Tk, messagebox
from components.graph import Graph
from components.airport_form import AirportForm
from components.route_form import RouteForm
from components.graph_button import GraphButton
from components.search_button import SearchButton
from components.search_form import SearchForm
from models.airport import Airport
from models.route import Route
import random

class App(Tk):
    """App
    
    This class is responsible for executing the entire application.
    """
    def __init__(self) -> None:
        super().__init__()
        self.title("Graph Airport")
        self.minsize(width=800, height=400)
        self.maxsize(width=800, height=400)

        airport1 = Airport(-3, 9, "Airport 1", "001")
        airport2 = Airport(0, 15, "Airport 2", "002")
        airport3 = Airport(5, 18, "Airport 3", "003")
        airport4 = Airport(0, 6, "Airport 4", "004")
        airport5 = Airport(3, 9, "Airport 5", "005")
        airport6 = Airport(5, 15, "Airport 6", "006")
        airport7 = Airport(10, 18, "Airport 7", "007")
        self.airports = [
            airport1,
            airport2,
            airport3,
            airport4,
            airport5,
            airport6,
            airport7
        ]

        
        self.routes = [
            Route(airport1, airport2, random.randint(200, 1200), random.randint(30, 240)),
            Route(airport1, airport5, random.randint(200, 1200), random.randint(30, 240)),
            Route(airport2, airport3, random.randint(200, 1200), random.randint(30, 240)),
            Route(airport3, airport6, random.randint(200, 1200), random.randint(30, 240)),
            Route(airport3, airport7, random.randint(200, 1200), random.randint(30, 240)),
            Route(airport2, airport6, random.randint(200, 1200), random.randint(30, 240)),
            Route(airport2, airport5, random.randint(200, 1200), random.randint(30, 240)),
            Route(airport1, airport4, random.randint(200, 1200), random.randint(30, 240)),
            Route(airport4, airport5, random.randint(200, 1200), random.randint(30, 240)),
            Route(airport5, airport6, random.randint(200, 1200), random.randint(30, 240)),
            Route(airport6, airport7, random.randint(200, 1200), random.randint(30, 240)),
        ]

        self.graph = Graph(self.airports, self.routes)
        self.airport_form = AirportForm(self, self.airports, self.save_airport)
        self.route_form = RouteForm(self, self.routes, self.save_route, self.find_airport_by_code, self.graph.remove_edge)
        self.graph_button = GraphButton(self, self.show_graph)
        self.search_button = SearchButton(self, self.show_search_form)

    def find_airport_by_code(self, code: str):
        """Find airport by code
        
        This method is responsible for finding an airport based on its code

        Args:
            code (str): airport code to be searched
        """
        for airport in self.airports:
            if airport.code == code:
                return airport
            
        return None

    def save_airport(self, code: str, coord_x: int, coord_y: int):
        """Save airport
        
        This method is responsible for converting an airport into a node to be graphed in the graph

        Args:
            code (str): airport code
            coord_x (int): location of the airport in x
            coord_y (int): location of the airport in y
        """
        self.graph.add_node(code, (coord_x, coord_y))

    def save_route(self, start, end, distance, time):
        """Save route
        
        This method saves a path to convert it into an edge

        Args:
            start: departure airport
            end: arrive airport
            distance: distance between airports
            time: time between airports
        """
        self.graph.add_edge(start, end, distance, time)

    def show_graph(self):
        """Show graph
        
        This method shows the graph of routes between airports
        """
        self.graph.render()

    def show_search_form(self):
        """Show search form
        
        This method executes the instance so that the route search form is displayed.
        """
        SearchForm(self, self.find_airport_by_code, self.search) 


    def search(self, from_airport: Airport, to_airport: Airport, search_by: int):
        """Search
        
        This method is responsible for displaying the result of the most optimal route

        Args:
            from_aiport (Airport): departure airport
            to_airport (Airport): arrival airport
            search_by (int): if you search by distance the indicator will be 1, but if you search by time the indicator will be 2
        """
        result = self.graph.search(from_airport, to_airport, search_by)
        message = ""
        for i, airport in enumerate(result):
            message += f"{i+1}. {airport}\n"

        messagebox.showinfo(title="Shortest route", message=message)



if __name__ == "__main__":
    app = App()
    app.mainloop()
