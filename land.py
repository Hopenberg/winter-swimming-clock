import time
from guizero import App, Text, TextBox, PushButton, Slider, Picture

def empty():
    return 0

def secondsToText(seconds):
    minutes = str(int(seconds / 60))
    secondsPart = str(seconds % 60)

    if len(secondsPart) == 1:
        secondsPart = "0" + secondsPart
    
    if (len(minutes) == 1):
        minutes = "0" + minutes

    return minutes + ":" + secondsPart

def textToSeconds(text):
    [minutes, seconds] = text.split(":")

    print([minutes, seconds])
    
    return int(minutes) * 60 + int(seconds)

def incrementTime(byAmount, stopAt):
    seconds = textToSeconds(timer.value)
    print(seconds)
    seconds = int(seconds) + byAmount

    if seconds >= stopAt:
        seconds = stopAt
        timer.cancel(incrementTime)

    timer.value = secondsToText(seconds)

def decrementTime(byAmount, stopAt):
    seconds = textToSeconds(timer.value)
    print(seconds)
    seconds = int(seconds) - byAmount

    if seconds <= stopAt:
        seconds = stopAt
        timer.cancel(decrementTime)

    timer.value = secondsToText(seconds)

def beginCountdown():
    timer.repeat(5, decrementTime, args=[1, 0])

def beginCountup():
    stopAt = textToSeconds(timer.value)
    timer.value = secondsToText(0)
    timer.repeat(5, incrementTime, args=[1, stopAt])

def readData():
    # code for reading the data from water
    return


app = App(title="Winter swimming clock", width=1000, height=600)

displayClock = "00:00"
timer = 0

timer = Text(app, text=displayClock, size=250, font="Courier New")
add_time = PushButton(app, text="Dodaj", command=incrementTime, args=[15, 600], width=45, image="icon_plus.png")
remove_time = PushButton(app, text="Odejmij", command=decrementTime, args=[15, 0], width=45, image="icon_minus.png")
button_start_down = PushButton(app, text="Liczenie w dół", command=beginCountdown, width=45, image="icon_down.png")
button_start_up = PushButton(app, text="Liczenie w górę", command=beginCountup, width=45, image="icon_up.png")

app.display()

