from tkinter import Frame, Tk, Entry, Label, Button, END, messagebox
from .list import List
from models.airport import Airport

class AirportForm(Frame):
    def __init__(self, master: Tk, data: list[Airport], save_airport) -> None:
        super().__init__(master, width=250, height=500)
        self.save_airport = save_airport
        self.airports = data

        self.list = List(self, 1, 0)
        self.render_items()

        self.render()

    def init_components(self):
        #title
        self.title_label = Label(self, text="Airports")
        self.title_label.grid(row=0, column=0, )

        # name
        self.name_label = Label(self, text="Name:")
        self.name_entry = Entry(self, width=33)
        self.name_label.grid(row=2, column=0)
        self.name_entry.grid(pady=5, row=2, column=1, columnspan=3)

        # # code
        self.code_label = Label(self, text="Code:")
        self.code_entry = Entry(self, width=33)
        self.code_label.grid(row=3, column=0)
        self.code_entry.grid(pady=5, row=3, column=1, columnspan=3)

        # coords
        self.x_label = Label(self, text="Coord x:")
        self.x_entry = Entry(self, width=12)
        self.x_label.grid(row=4, column=0)
        self.x_entry.grid(pady=5,row=4, column=1)

        self.y_label = Label(self, text="Coord y:")
        self.y_entry = Entry(self, width=13)
        self.y_label.grid(row=4, column=2)
        self.y_entry.grid(padx=2,row=4, column=3)

        # button
        self.save_button = Button(self, text="Save", width=37, command=self.save_command)
        self.save_button.grid(pady=5, row=5, column=0, columnspan=4)

    def save_command(self):
        try:
            name = self.name_entry.get()
            code = self.code_entry.get()
            coord_x = float(self.x_entry.get())
            coord_y = float(self.y_entry.get())

            self.save_airport(name, code, coord_x, coord_y)
            
            # reset fields
            self.name_entry.delete(0, END)
            self.code_entry.delete(0, END)
            self.x_entry.delete(0, END)
            self.y_entry.delete(0, END)

            # clean and fill up the list
            self.airports.append(Airport(coord_x, coord_y, name, code))
            self.render_items()
        except:
            messagebox.showerror(title='Bad Request', message='All fields are required')

    def render_items(self):
        self.list.delete(0, END)
        for airport in self.airports:
            self.list.add(f"{airport.code} - {airport.name}")


    def render(self):
        self.init_components()
        self.grid(padx=10, row=0, column=0)