# play_gong.py
# usage: "python play_gong.py 20" or "python play_gong.py"

import sys
import webbrowser
from time import sleep
import datetime as dt


minutes_between = 30 if len(sys.argv) == 1 else int(sys.argv[1])
print("This script plays a gong every ", minutes_between, " minutes.")
print("Press Ctrl + C to quit.")

while True:
    curr_time = dt.datetime.now()
    # Don't play at night.
    if curr_time.time() <= dt.time(23,00) and curr_time.time() >= dt.time(8,00):
        webbrowser.open_new("https://www.youtube.com/watch?v=lYfYa9rK7sE")
    sleep(60 * minutes_between)
