from tkinter import Listbox, Tk, END

class List(Listbox):
    def __init__(self, master: Tk, row: int, column: int) -> None:
        super().__init__(master, width=40)
        self.row = row
        self.column= column
        self.render()

    def add(self, item: str):
        self.insert(END, item)

    def render(self):
        self.grid(row= self.row, column=self.column, columnspan=4)