from tkinter import Frame, Tk, Entry, Label, Button
from .list import List

class AirportForm(Frame):
    def __init__(self, master: Tk) -> None:
        super().__init__(master, width=450, height=600)
        self.y = 250
        self.list = List(self)

        self.list.add('Test1')
        self.list.add('Test2')

        self.render()

    def init_components(self):
        #title
        self.title_label = Label(self, text="Airports")
        self.title_label.place(x = 0, y = 0)

        # name
        self.name_label = Label(self, text="Name")
        self.name_entry = Entry(self, width=100)
        self.name_label.place(x = 10, y = self.y)
        self.name_entry.place(x = 10, y = self.y + 20)

        # code
        self.code_label = Label(self, text="Code")
        self.code_entry = Entry(self, width=100)
        self.code_label.place(x = 10, y = self.y + 50)
        self.code_entry.place(x = 10, y = self.y + 70)

        # coords
        self.x_label = Label(self, text="X")
        self.x_entry = Entry(self, width=50)
        self.x_label.place(x = 10, y = self.y + 100)
        self.x_entry.place(x = 10, y = self.y + 120)

        self.y_label = Label(self, text="Y")
        self.y_entry = Entry(self, width=50)
        self.y_label.place(x = 10, y = self.y + 150)
        self.y_entry.place(x = 10, y = self.y + 170)

        # button
        self.save_button = Button(self, text="Save")
        self.save_button.place(x = 10, y = self.y + 200)

    def render(self):
        self.place(x=10, y=10)
        self.init_components()
        pass