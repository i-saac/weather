from gui import Gui
from scraper import Scraper
import tkinter as tk

# attempt to read address.txt
try:
    file = open('address.txt', 'r')
    address = file.read()
    file.close()
except FileNotFoundError:
    address = None

# catch no address error code
if address == 'None':
    address = None

# initialize root
root = tk.Tk()

# create gui object with address
user_interface = Gui(root, address)

# main root loop
root.mainloop()

# create scraper based on last address in user_interface
new_address = user_interface.get_address()
web_scraper = Scraper(new_address)

# write address if there is one, otherwise write none
file = open('address.txt', 'w')
if web_scraper.is_valid_address():
    file.write(new_address)
else:
    file.write('None')
file.close()
