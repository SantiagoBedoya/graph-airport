from tkinter import Canvas
import random


class Drawer(Canvas):
    def __init__(self, master, width, height, x, y) -> None:
        super().__init__(
            master,
            highlightthickness=1,
            highlightbackground="gray40",
        )
        self.place(relwidth=width, relheight=height, x=x, y=y)

    def draw_airport(self, airport):
        self.create_oval(airport.x, airport.y, airport.x + 60, airport.y + 60)
        self.create_text(airport.x + 5, airport.y + 30, anchor="w", text=airport.name)
        pass

    def draw_route(self, start_airport, end_airport):
        color = f"#{random.randrange(256**3):06x}"
        self.create_line(
            start_airport.x + 20,
            start_airport.y + 20,
            end_airport.x + 20,
            end_airport.y + 20,
            fill=color,
        )
