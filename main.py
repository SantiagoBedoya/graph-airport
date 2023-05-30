from tkinter import Tk


class App:
    def __init__(self) -> None:
        self.t = Tk()

    def render(self):
        self.t.title("Graph Airport")
        self.t.minsize(width=650, height=650)
        

        self.t.mainloop()

app = App()
app.render()