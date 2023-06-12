from tkinter import Frame, Tk, Entry, Label, Button
from .list import List

class AirportForm(Frame):
    def __init__(self, master: Tk) -> None:
        super().__init__(master, width=250, height=500)
        self.list = List(self)

        self.list.add('Test1')
        self.list.add('Test2')
        self.list.add('test3')

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

        # # coords
        self.x_label = Label(self, text="Coord x:")
        self.x_entry = Entry(self, width=12)
        self.x_label.grid(row=4, column=0)
        self.x_entry.grid(pady=5,row=4, column=1)

        self.y_label = Label(self, text="Coord y:")
        self.y_entry = Entry(self, width=13)
        self.y_label.grid(row=4, column=2)
        self.y_entry.grid(padx=2,row=4, column=3)

        # button
        self.save_button = Button(self, text="Save", width=37)
        self.save_button.grid(pady=5, row=5, column=0, columnspan=4)

    def render(self):
        self.init_components()
        self.grid(padx=4, row=0, column=0)