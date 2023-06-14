from tkinter import Button, Tk

class SearchButton(Button):
    """Search Button
    
    This class renders a button that is responsible for displaying the search form

    Args:
        command: Action to be executed when the button is clicked
    """
    
    def __init__(self, master: Tk, command: any, ) -> None:
        super().__init__(master, text="Search", command=command)

        self.render()

    def render(self):
        """Render
        
        Show the button component with its location
        """
        self.grid(pady=10, row=2, column=1, columnspan=1)