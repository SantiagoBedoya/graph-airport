from tkinter import Listbox, Tk, END, Label

class List(Listbox):
    def __init__(self, master: Tk) -> None:
        super().__init__(master, width=400)
        self.render()

    def add(self, item: str):
        self.insert(END, item)

    def render(self):
        self.place(x = 0, y = 30)