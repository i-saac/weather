from gui import Gui
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

# write address if there is one, otherwise write none
file = open('address.txt', 'w')
if user_interface.address is not None:
    file.write(user_interface.address)
else:
    file.write('None')
file.close()
