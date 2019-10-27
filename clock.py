import datetime, time

# Infinite loop to constantly keep getting the current time
while (True):
    # Wait 1 second before running the rest of the code
    time.sleep(1)

    # Print the current time in Hours:Minutes:Seconds
    print(datetime.datetime.now().time().strftime('%H:%M:%S'))