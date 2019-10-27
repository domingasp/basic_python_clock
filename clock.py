############ IMPORTS ############
import math
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

        # Create the hour, minute and second rectangle
        self.hourRectangle = self.rectangeCanvas.create_rectangle(3, 3, 0, 18, fill = 'green')
        self.minuteRectangle = self.rectangeCanvas.create_rectangle(3, 23, 0, 38, fill = 'blue')
        self.secondRectangle = self.rectangeCanvas.create_rectangle(3, 43, 0, 58, fill = 'magenta')

        # Canvas for the circle clock
        self.circleCanvas = tk.Canvas(self.master, width = 360, height = 360)
        self.circleCanvas.pack()

        # Create the hour, minute and second hands
        self.hourHand = self.circleCanvas.create_line(180, 180, 0, 90, fill = 'green')
        self.minuteHand = self.circleCanvas.create_line(180, 180, 0, 140, fill = 'blue')
        self.secondHand = self.circleCanvas.create_line(180, 180, 0, 180, fill = 'magenta')

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

    # Calculates the seconds hand angle and updates the GUI to reflect the new time
    hour_angle_in_radians = ((hour % 12) * 30 - 90) * math.pi / 180
    hour_line_length = 90
    hour_end_x = 180 + hour_line_length * math.cos(hour_angle_in_radians)
    hour_end_y = 180 + hour_line_length * math.sin(hour_angle_in_radians)
    gui.circleCanvas.coords(gui.hourHand, 180, 180, hour_end_x, hour_end_y)

    # Calculates the seconds hand angle and updates the GUI to reflect the new time
    minute_angle_in_radians = (minute * 6 - 90) * math.pi / 180
    minute_line_length = 140
    minute_end_x = 180 + minute_line_length * math.cos(minute_angle_in_radians)
    minute_end_y = 180 + minute_line_length * math.sin(minute_angle_in_radians)
    gui.circleCanvas.coords(gui.minuteHand, 180, 180, minute_end_x, minute_end_y)

    # Calculates the seconds hand angle and updates the GUI to reflect the new time
    second_angle_in_radians = (second * 6 - 90) * math.pi / 180
    second_line_length = 180
    second_end_x = 180 + second_line_length * math.cos(second_angle_in_radians)
    second_end_y = 180 + second_line_length * math.sin(second_angle_in_radians)
    gui.circleCanvas.coords(gui.secondHand, 180, 180, second_end_x, second_end_y)

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