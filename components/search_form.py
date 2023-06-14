from tkinter import Toplevel, Entry, Label, Radiobutton, IntVar, Button, messagebox


class SearchForm(Toplevel):
    def __init__(self, master, find_airport_by_code, search) -> None:
        super().__init__(master, width=500)
        self.search_by_var = IntVar()
        self.search = search
        self.find_airport_by_code = find_airport_by_code

        self.init_components()

    def init_components(self):
        # from
        from_label = Label(self, text="From")
        from_label.grid(row=0, column=0)
        self.from_entry = Entry(self, width=100)
        self.from_entry.grid(row=1, column=0)

        # to
        to_label = Label(self, text="To")
        to_label.grid(row=2, column=0)
        self.to_entry = Entry(self, width=100)
        self.to_entry.grid(row=3, column=0)

        # search by
        search_by_label = Label(self, text="Search by")
        search_by_label.grid(row=4, column=0)
        time_radio_button = Radiobutton(
            self, text="Time", value=1, variable=self.search_by_var
        )
        time_radio_button.grid(row=5, column=0)
        distance_radio_button = Radiobutton(
            self, text="Distance", value=2, variable=self.search_by_var
        )
        distance_radio_button.grid(row=6, column=0)

        # search button
        search_button = Button(self, text="Search", command=self.search_command)
        search_button.grid(row=7, column=0)

    def search_command(self):
        
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
