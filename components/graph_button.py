from tkinter import Button, Tk

class GraphButton(Button):
    def __init__(self, master: Tk, command: any, ) -> None:
        super().__init__(master, text="Show Graph", command=command)

        self.render()

    def render(self):
        self.grid(pady=10, row=2, column=0, columnspan=2)