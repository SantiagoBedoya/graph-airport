from tkinter import Listbox, Tk, END, Label

class List(Listbox):
    def __init__(self, master: Tk) -> None:
        super().__init__(master, width=40 )
        self.render()

    def add(self, item: str):
        self.insert(END, item)

    def render(self):
        self.grid(row=1, column=0, columnspan=4)