
import tkinter as tk # Import the tkinter library for creating the GUI
from time import strftime # Import the strftime function from the time module to format the time and date

root = tk.Tk() # Create the main application window
root.title("Digital Clock") # Set the title of the window

def time():
    string = strftime('%H:%M:%S %p \n %D') # Get the current time and date in the specified format
    lable.config(text=string) # Update the label with the current time and date
    lable.after(1000, time) # Schedule the time function to be called again after 1000 milliseconds (1 second)

lable = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white') # Create a label to display the time and date
lable.pack(anchor='center') # Center the label in the window

time() # Call the time function to start updating the label with the current time and date

root.mainloop() # Start the main event loop to run the application
