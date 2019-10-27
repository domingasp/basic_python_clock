############ IMPORTS ############
import datetime, time

# Main function which runs an infinite loop with a frequency of 1 second. Constantly getting the current time.
def main():
    # Infinite loop to constantly keep getting the current time
    while (True):
        # Wait 1 second before running the rest of the code
        time.sleep(1)

        # Gets the current time. Assigns the hour, minute and second to their respective variables to be used later.
        currentTime = datetime.datetime.now().time()
        hour = currentTime.hour
        minute = currentTime.minute
        second = currentTime.second

        # Print the current time in Hours:Minutes:Seconds
        print(str(hour) + ':' + str(minute) + ':' + str(second))

############ STARTS THE PROGRAM ############
if __name__ == '__main__':
    main()