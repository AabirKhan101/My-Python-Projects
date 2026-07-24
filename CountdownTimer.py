# Countdown timer program
import time

tyme = int(input("Enter the time in seconds for which you want to pause : "))

for t in range(tyme, 0, -1):
    seconds = t % 60   # t is the amount of time specified in the time variable, find the remainder of that with 60. We do this because we dont want the seconds to go above 60
    minutes = int((t / 60)) % 60  #if we dont type cast it as an integer, it will prouce float values. We divide t by 60 since one minute has 60 seconds and we find the modulus of that with 60 since we dont want minutes to exceed 60
    hours = int(t / 3600)  # we typecast the time as int otherwise it will produce float values and divide it by 3600 since one hour has 3600 seconds. We did not take the modulus by 24 as we dont have days in our countdown timer.
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Hello")
