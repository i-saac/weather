import tkinter as tk
from scraper import Scraper


class Gui:

    def __init__(self, root, address):
        # initialize root and title
        self.root = root
        self.root.resizable(0, 0)
        self.root.title('Weather')

        # initialize base canvas
        self.canvas = tk.Canvas(self.root, width=1000, height=500, bg='light blue')
        self.canvas.pack()

        # initialize address
        self.address = address

        # determine if address was loaded from file
        if self.address is None:
            # if none was loaded initialize entry UI
            self.init_entry_ui()
        else:
            # otherwise load weather UI
            self.init_weather_ui()

    # initialize address entry UI
    def init_entry_ui(self):
        # clear canvas
        self.clear_canvas()

        # reset address
        self.address = None

        # create prompt text
        self.prompt_text = self.canvas.create_text(500, 35, text='Enter Address Below:')

        # create address entry text box
        self.address_entry_box = tk.Text(self.canvas, bg='white')
        self.address_entry_box.place(width=600, height=200, x=200, y=50)

        # create find weather button
        self.init_weather_button = tk.Button(self.canvas, text='Get Weather', bg='white', command=self.init_weather_ui)
        self.init_weather_button.place(width=300, height=100, x=350, y=300)

    # initialize weather UI
    def init_weather_ui(self):
        # get address from text entry box
        self.address = self.address_entry_box.get('1.0', 'end-1c') if self.address is None else self.address

        # clear canvas
        self.clear_canvas()

        # set up scraper
        self.scraper = Scraper(self.address)

        # create text objects to display location and weather
        self.location_text = self.canvas.create_text(500, 100, text=self.scraper.get_location())
        if self.scraper.get_location() != 'Error: Invalid Address':
            self.forecast_text = self.canvas.create_text(500, 115, text=self.scraper.get_forecast())
            self.temp_c_text = self.canvas.create_text(500, 130, text=self.scraper.get_temp_f())
            self.temp_f_text = self.canvas.create_text(500, 145, text=self.scraper.get_temp_c())

        # initialize reset button
        self.init_reset_button = tk.Button(self.canvas, text='Reset Slot', bg='white', command=self.init_entry_ui)
        self.init_reset_button.place(width=300, height=100, x=350, y=300)

    # clear canvas
    def clear_canvas(self):
        # destroy all widgets
        for widget in self.canvas.winfo_children():
            widget.destroy()

        # destroy text created by weather UI state
        try:
            self.canvas.delete(self.location_text)
            self.canvas.delete(self.forecast_text)
            self.canvas.delete(self.temp_c_text)
            self.canvas.delete(self.temp_f_text)
        except AttributeError:
            pass

        # destroy text created by entry UI state
        try:
            self.canvas.delete(self.prompt_text)
        except AttributeError:
            pass
