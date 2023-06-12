from tkinter import Frame, Tk, Entry, Label, Button

class RouteForm(Frame):
    def __init__(self, master: Tk) -> None:
        super().__init__(master, width=250, height=500)
        self.render()

    def init_components(self):
        #title
        self.title_label = Label(self, text="Routes")
        self.title_label.grid(row=0, column=0)

        # start
        self.start_label = Label(self, text="Start:")
        self.start_entry = Entry(self, width=33)
        self.start_label.grid(row=1, column=0)
        self.start_entry.grid(pady=5, row=1, column=1, columnspan=3)

        # end
        self.end_label = Label(self, text="End:")
        self.end_entry = Entry(self, width=33)
        self.end_label.grid(row=2, column=0)
        self.end_entry.grid(pady=5, row=2, column=1, columnspan=3)

         # distance
        self.distance_label = Label(self, text="Distance")
        self.distance_entry = Entry(self, width=14)
        self.distance_label.grid(row=3, column=0)
        self.distance_entry.grid(pady=5,row=3, column=1)

        # time
        self.time_label = Label(self, text="Time:")
        self.time_entry = Entry(self, width=14)
        self.time_label.grid(row=3, column=2)
        self.time_entry.grid(padx=2,row=3, column=3)

        # button
        self.save_button = Button(self, text="Save", width=37)
        self.save_button.grid(pady=5, row=5, column=0, columnspan=4)

    def render(self):
        self.init_components()
        self.grid(pady=50, row=1, column=0)