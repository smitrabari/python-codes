# Countdown Timer Program
import time

my_time =int(input("Enter Timer in Seconds : ")) # input of time

for x in range(my_time,0,-1): # loop going backward
    seconds = x % 60 # for seconds
    minutes = int(x/60) % 60 # minutes
    hour = int(x / 3600) # hours
    print(f"{hour:02}:{minutes:02}:{seconds:02}")
    time.sleep(1) # time Function

print("Time up!!")