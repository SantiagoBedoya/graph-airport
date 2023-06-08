from tkinter import Frame, Tk

class RouteForm(Frame):
    def __init__(self, master: Tk) -> None:
        super().__init__(master, width=450, height=600, bg='#000')
        self.render()

    def render(self):
        self.place(x=500, y=10)
        pass