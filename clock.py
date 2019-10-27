import datetime, time

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