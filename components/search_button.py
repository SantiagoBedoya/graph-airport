from tkinter import Button, Tk

class SearchButton(Button):
    def __init__(self, master: Tk, command: any, ) -> None:
        super().__init__(master, text="Search", command=command)

        self.render()

    def render(self):
        self.grid(pady=10, row=2, column=1, columnspan=1)