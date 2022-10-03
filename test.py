import time
import datetime

import timingmodule

start_time = None
start_time = datetime.datetime.now()

time.sleep(5)

X = timingmodule.TimeSpentInApp(start_time)

print(f"You spent a total of {X} seconds in the APP")