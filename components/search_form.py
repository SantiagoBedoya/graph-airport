from tkinter import Toplevel, Entry, Label, Radiobutton, IntVar, Button, messagebox


class SearchForm(Toplevel):
    """Search form
    
    This class contains the components and methods necessary to search for optimal routes.
    """
    def __init__(self, master, find_airport_by_code, search) -> None:
        super().__init__(master, width=300)
        self.search_by_var = IntVar()
        self.search = search
        self.find_airport_by_code = find_airport_by_code

        self.init_components()

    def init_components(self):
        """Init components
        
        This function initializes the form components
        """
        # from
        from_label = Label(self, text="From")
        from_label.grid(row=0, column=0)
        self.from_entry = Entry(self, width=30)
        self.from_entry.grid(padx=5, row=0, column=1, columnspan=2)

        # to
        to_label = Label(self, text="To")
        to_label.grid(row=1, column=0)
        self.to_entry = Entry(self, width=30)
        self.to_entry.grid(pady=5, row=1, column=1, columnspan=2)

        # search by
        search_by_label = Label(self, text="Search by")
        search_by_label.grid(row=2, column=0)
        time_radio_button = Radiobutton(
            self, text="Time", value=1, variable=self.search_by_var
        )
        time_radio_button.grid(row=2, column=1)
        distance_radio_button = Radiobutton(
            self, text="Distance", value=2, variable=self.search_by_var
        )
        distance_radio_button.grid(row=2, column=2)

        # search button
        search_button = Button(self, text="Search", command=self.search_command)
        search_button.grid(pady=5, row=3, column=0, columnspan= 3)

    def search_command(self):
        """Search command
        
        This method is responsible for executing the action so that the most optimal route is displayed.
        """
        from_val = self.from_entry.get()
        from_airport = self.find_airport_by_code(from_val)
        if from_airport == None:
            messagebox.showerror(title="Airport not found", message=f"From Airport with code {from_val} not found")
            return

        to_val = self.to_entry.get()
        to_airport = self.find_airport_by_code(to_val)
        if to_airport == None:
            messagebox.showerror(title="Airport not found", message=f"To Airport with code {from_val} not found")
            return

        search_by_val = self.search_by_var.get()
        
        
        self.search(from_airport, to_airport, search_by_val)
