############ IMPORTS ############
import datetime, time
import tkinter as tk

# GUI class to handle the creation of the GUI
class GUI:
    def __init__(self, master):
        self.master = master

        # Set the title of the main window
        self.master.title('Clock')

# Called to get the current time and alter the gui to reflect the time
def getCurrentTime(root, gui):
    # Gets the current time. Assigns the hour, minute and second to their respective variables to be used later.
    currentTime = datetime.datetime.now().time()
    hour = currentTime.hour
    minute = currentTime.minute
    second = currentTime.second

    # Print the current time in Hours:Minutes:Seconds
    print(str(hour) + ':' + str(minute) + ':' + str(second))

    # Reschedules itself to run again after 1 minute, thus is constantly being called
    root.after(1000, lambda: getCurrentTime(root, gui))

# Main function which runs an infinite loop with a frequency of 1 second. Constantly getting the current time.
def main():
    # Creates the root object
    root = tk.Tk()

    # Creates the GUI
    gui = GUI(root)

    # Gets the current time to initialise the infinite callback loop every second, and initialises the GUI.
    getCurrentTime(root, gui)

    # Runs the root mainloop
    root.mainloop()

############ STARTS THE PROGRAM ############
if __name__ == '__main__':
    main()