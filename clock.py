############ IMPORTS ############
import datetime, time
import tkinter as tk

# GUI class to handle the creation of the GUI
class GUI:
    def __init__(self, master):
        self.master = master

        # Set the title of the main window
        self.master.title('Clock')

        # Create the canvas where the rectange clock will be displayed
        self.rectangeCanvas = tk.Canvas(self.master, width = 360, height = 58)
        self.rectangeCanvas.pack()

        # Create the hour rectangle (x1 = beginning position, y1 = beginning position, x2 = current time, y2 = end position controls the height)
        self.hourRectangle = self.rectangeCanvas.create_rectangle(3, 3, 0, 18, fill = 'green')

        # Create the minute rectangle (x1 = beginning position, y1 = beginning position, x2 = current time, y2 = end position controls the height)
        self.minuteRectangle = self.rectangeCanvas.create_rectangle(3, 23, 0, 38, fill = 'blue')

        # Create the second rectangle (x1 = beginning position, y1 = beginning position, x2 = current time, y2 = end position controls the height)
        self.secondRectangle = self.rectangeCanvas.create_rectangle(3, 43, 0, 58, fill = 'yellow')

        # Canvas for the circle clock
        self.circleCanvas = tk.Canvas(self.master, width = 360, height = 360)
        self.circleCanvas.pack()

        self.secondHand = self.circleCanvas.create_rectangle(180, 180, 180, 0)

# Called to get the current time and alter the gui to reflect the time
def getCurrentTime(root, gui):
    # Gets the current time. Assigns the hour, minute and second to their respective variables to be used later.
    currentTime = datetime.datetime.now().time()
    hour = currentTime.hour
    minute = currentTime.minute
    second = currentTime.second

    # Updates the GUI for the rectangle clock with the new time
    gui.rectangeCanvas.coords(gui.hourRectangle, 3, 3, 0 + (hour * 15), 18)
    gui.rectangeCanvas.coords(gui.minuteRectangle, 3, 23, 0 + (minute * 6), 38)
    gui.rectangeCanvas.coords(gui.secondRectangle, 3, 43, 0 + (second * 6), 58)

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

    # Gets the current time to initialise the infinite callback loop every second, and updates the GUI.
    getCurrentTime(root, gui)

    # Runs the root mainloop
    root.mainloop()

############ STARTS THE PROGRAM ############
if __name__ == '__main__':
    main()