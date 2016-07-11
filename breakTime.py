import webbrowser
import time

totalBreaks = 2
currentBreak = 0
while currentBreak < totalBreaks:
    print "This program started on " + time.ctime()
    time.sleep(5)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    currentBreak += 1
