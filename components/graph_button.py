from tkinter import Button, Tk

class GraphButton(Button):
    """Graph Button
    
    This class renders a button that is responsible for displaying the graph

    Args:
        command: Action to be executed when the button is clicked
    """
    def __init__(self, master: Tk, command: any, ) -> None:
        super().__init__(master, text="Show Graph", command=command)

        self.render()

    def render(self):
        """Render
        
        Show the button component with its location
        """
        self.grid(pady=10, row=2, column=0, columnspan=1)