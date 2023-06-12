from tkinter import Frame, Tk

class RouteForm(Frame):
    def __init__(self, master: Tk) -> None:
        super().__init__(master, width=300, height=500)
        self.render()

    def render(self):
        self.grid(row=1, column=0)