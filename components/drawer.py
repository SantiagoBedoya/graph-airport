from tkinter import Canvas
from models.airport import Airport
import tkinter as tk
import random


class Drawer(Canvas):
    def __init__(self, master:any) -> None:
        super().__init__(
            master,
            highlightthickness=1,
            highlightbackground="gray40",
        )
        self.pack(expand=True, fill= tk.BOTH, padx= 12, pady=12)

    def draw_airport(self, airport:Airport):
        self.create_oval(airport.x, airport.y, airport.x + 60, airport.y + 60)
        self.create_text(airport.x + 5, airport.y + 30, anchor="w", text=airport.name)
        pass

    def draw_route(self, start_airport:int, end_airport:int):
        color = f"#{random.randrange(256**3):06x}"
        self.create_line(
            start_airport.x + 20,
            start_airport.y + 20,
            end_airport.x + 20,
            end_airport.y + 20,
            fill=color,
        )
