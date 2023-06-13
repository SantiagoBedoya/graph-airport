from tkinter import Frame, Tk, Entry, Label, Button, END, messagebox
from models.route import Route
from .list import List

class RouteForm(Frame):
    def __init__(self, master: Tk, data: list[Route], save_route, find_airport_by_code) -> None:
        super().__init__(master, width=250, height=500)
        self.save_route = save_route
        self.find_airport_by_code = find_airport_by_code

        self.list = List(self, 1, 0)
        self.render_items()

        self.routes = data
        self.render()

    def init_components(self):
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
        self.save_button = Button(self, text="Save", width=37, command=self.save_command)
        self.save_button.grid(pady=5, row=5, column=0, columnspan=4)

    def save_command(self):
        try:
            start = self.start_entry.get()
            end = self.end_entry.get()
            distance = float(self.distance_entry.get())
            time = float(self.time_entry.get())

            start_airport = self.find_airport_by_code(start)
            if start_airport == None:
                messagebox.showerror(title = 'Airport Not Found', message=f"Airport with code: {start} does not exist")

            end_airport = self.find_airport_by_code(end)
            if end_airport == None:
                messagebox.showerror(title = 'Airport Not Found', message = f"Airport with code: {end} does not exist")

            self.routes.append(Route(start_airport, end_airport, distance, time))
            self.save_route(start, end, distance, time)

            # # reset fields
            self.start_entry.delete(0, END)
            self.end_entry.delete(0, END)
            self.distance_entry.delete(0, END)
            self.time_entry.delete(0, END)
        except:
            messagebox.showerror(title='Bad Request', message="All fields are required")
    
    def render_items(self):
        self.list.delete(0, END)
        for route in self.routes:
            self.list.add(f"{route.start.code} => {route.end.code}: {route.distance}km ({route.time})")
        pass

    def render(self):
        self.init_components()
        self.grid(padx=50, row=0, column=1)