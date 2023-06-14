from tkinter import Frame, Tk, Entry, Label, Button, END, messagebox
from models.route import Route
from .list import List

class RouteForm(Frame):
    """Route form.
    
    This class contains the fields and components that make up the form to create the airports.

    Args:
        data list(Route): List of routes to display on the screen
        save_route: Function that is responsible for displaying the route in the graph
        find_airport_by_code: This function is responsible for finding an airport based on the code
    """

    def __init__(self, master: Tk, data: list[Route], save_route, find_airport_by_code, remove_edge) -> None:
        super().__init__(master, width=250, height=500)
        self.save_route = save_route
        self.find_airport_by_code = find_airport_by_code
        self.routes = data
        self.selected_item = None
        self.remove_edge = remove_edge

        self.list = List(self, 1, 0)
        self.render_items()

        self.render()

    def init_components(self):
        """Init components
        
        This function initializes the form components
        """

        #title
        self.title_label = Label(self, text="Routes")
        self.title_label.grid(row=0, column=0)

        # start
        self.start_label = Label(self, text="Start:")
        self.start_entry = Entry(self, width=33)
        self.start_label.grid(row=2, column=0)
        self.start_entry.grid(pady=5, row=2, column=1, columnspan=3)

        # end
        self.end_label = Label(self, text="End:")
        self.end_entry = Entry(self, width=33)
        self.end_label.grid(row=3, column=0)
        self.end_entry.grid(pady=5, row=3, column=1, columnspan=3)

         # distance
        self.distance_label = Label(self, text="Distance")
        self.distance_entry = Entry(self, width=14)
        self.distance_label.grid(row=4, column=0)
        self.distance_entry.grid(pady=5,row=4, column=1)

        # time
        self.time_label = Label(self, text="Time:")
        self.time_entry = Entry(self, width=14)
        self.time_label.grid(row=4, column=2)
        self.time_entry.grid(padx=2,row=4, column=3)

        # button
        self.save_button = Button(self, text="Save", width=10, command=self.save_command)
        self.save_button.grid(pady=5, row=5, column=0, columnspan=2)
        self.update_button = Button(self, text="Update", width=10, command=self.update_route)
        self.update_button.grid(pady=5, row=5, column=3, columnspan=2)

    def save_command(self):
        """Save command
        
        This function is responsible for creating a new route and adding it to the list
        """

        try:
            start = self.start_entry.get()
            end = self.end_entry.get()
            distance = float(self.distance_entry.get())
            time = float(self.time_entry.get())

            start_airport = self.find_airport_by_code(start)
            if start_airport == None:
                messagebox.showerror(title = 'Airport Not Found', message=f"Airport with code: {start} does not exist")
                return

            end_airport = self.find_airport_by_code(end)
            if end_airport == None:
                messagebox.showerror(title = 'Airport Not Found', message = f"Airport with code: {end} does not exist")
                return

            self.routes.append(Route(start_airport, end_airport, distance, time))
            self.save_route(start, end, distance, time)
            self.render_items()

            # reset fields
            self.start_entry.delete(0, END)
            self.end_entry.delete(0, END)
            self.distance_entry.delete(0, END)
            self.time_entry.delete(0, END)
        except:
            messagebox.showerror(title='Bad Request', message="All fields are required")
    
    def select_item(self, event):
        """Select item
        
        This method is responsible for selecting a route to be updated
        """
        selection = event.widget.curselection()
        if len(selection) == 0:
            return
        data = str(event.widget.get(selection[0]))
        fields = data.split(" => ")
        fields2 = fields[1].split(": ")
        fields3 = fields2[1].split("km (")
        fields4 = fields3[1].split("m")

        # fields
        start = fields[0]
        end = fields2[0]
        distance = float(fields3[0])
        time = float(fields4[0]) 

        # clean entries
        self.start_entry.delete(0, END)
        self.end_entry.delete(0, END)
        self.distance_entry.delete(0, END)
        self.time_entry.delete(0, END)

        # set value to entries
        self.start_entry.insert(0, start)
        self.end_entry.insert(0, end)
        self.distance_entry.insert(0, distance)
        self.time_entry.insert(0, time)

        self.selected_item = Route(self.find_airport_by_code(start), self.find_airport_by_code(end), distance, time)

    

    def update_route(self):
        """Update route
        
        This method is responsible for updating a route by modifying all its attributes
        """
        try:
            start = self.start_entry.get()
            end = self.end_entry.get()
            distance = float(self.distance_entry.get())
            time = float(self.time_entry.get())

            start_airport = self.find_airport_by_code(start)
            if start_airport == None:
                messagebox.showerror(title = 'Airport Not Found', message=f"Airport with code: {start} does not exist")
                return

            end_airport = self.find_airport_by_code(end)
            if end_airport == None:
                messagebox.showerror(title = 'Airport Not Found', message = f"Airport with code: {end} does not exist")
                return

            for route in self.routes:
                if route.start.code == self.selected_item.start.code and route.end.code == self.selected_item.end.code:
                    index = self.routes.index(route)
                    del self.routes[index]
                    self.remove_edge(self.selected_item.start, self.selected_item.end)
            
            
            self.routes.append(Route(start_airport, end_airport, distance, time))
            self.save_route(start, end, distance, time)
            self.render_items()

            # reset fields
            self.start_entry.delete(0, END)
            self.end_entry.delete(0, END)
            self.distance_entry.delete(0, END)
            self.time_entry.delete(0, END)

            
        except:
            messagebox.showerror(title='Bad Request', message="All fields are required") 
        
        
    def set_listeners(self):
        """Set listeners
        
        This method is responsible for listening to the events that happen
        """
        self.list.bind("<<ListboxSelect>>", self.select_item)

    def render_items(self):
        """Render items
        
        This method is responsible for listing the routes that exist
        """
        self.list.delete(0, END)
        for route in self.routes:
            self.list.add(f"{route.start.code} => {route.end.code}: {route.distance}km ({route.time}m)")        

    def render(self):
        """Render
        
        This method is responsible for displaying the form with all its components.
        """
        self.init_components()
        self.set_listeners()
        self.grid(padx=40, row=0, column=1)