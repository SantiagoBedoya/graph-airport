from tkinter import Listbox, Tk, END

class List(Listbox):
    """Lists
    
    This class is responsible for rendering the lists in the forms

    Args:
        row (int): row in which the listbox is located
        column (int): column which the listbox is located
    """
    def __init__(self, master: Tk, row: int, column: int) -> None:
        super().__init__(master, width=40)
        self.row = row
        self.column= column
        self.render()

    def add(self, item: str):
        """Add
        
        This method is responsible for adding items to the list

        Args:
            item (str): item to be added
        """
        self.insert(END, item)

    def render(self):
        """Render
        
        This method is responsible for displaying the listbox with the items listed
        """
        self.grid(row= self.row, column=self.column, columnspan=4)