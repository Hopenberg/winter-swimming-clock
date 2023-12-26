import time
from guizero import App, Text, TextBox, PushButton, Slider, Picture, Box

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


app = App(title="Winter swimming clock", width=1024, height=600)

displayClock = "00:00"
displayHeartrate = "123 <3"
displayTemperature = "23 C"
timer = 0
padding = 10

timer_box = Box(app, align="top", width="fill")
timer = Text(timer_box, text=displayClock, size=250, font="Lato", color="#c3b091", width="fill")

buttons_box = Box(app, align="left", width="fill")

buttons_box_top = Box(buttons_box, align="top")
buttons_box_bottom = Box(buttons_box, align="bottom")

left_pad = Box(buttons_box_top, align="left", height="fill", width=padding)
add_time = PushButton(buttons_box_top, 
                      text="Dodaj", 
                      command=incrementTime, 
                      args=[15, 600], 
                      width=45, 
                      image="icon_plus.png", 
                      align="left")

left_pad = Box(buttons_box_top, align="left", height="fill", width=padding)
remove_time = PushButton(buttons_box_top, 
                         text="Odejmij", 
                         command=decrementTime, 
                         args=[15, 0], 
                         width=45, 
                         image="icon_minus.png", 
                         align="left")

bootom_pad = Box(buttons_box_top, align="bottom", height=padding*8)

left_pad = Box(buttons_box_bottom, align="left", height="fill", width=padding)
button_start_up = PushButton(buttons_box_bottom, 
                             text="Liczenie w górę", 
                             command=beginCountup, 
                             width=45, 
                             image="icon_up.png", 
                             align="left")

left_pad = Box(buttons_box_bottom, align="left", height="fill", width=padding)
button_start_down = PushButton(buttons_box_bottom, 
                               text="Liczenie w dół", 
                               command=beginCountdown, 
                               width=45, 
                               image="icon_down.png", 
                               align="left")


data_box = Box(app, align="left", width="fill")

heartrate = Text(data_box, text=displayHeartrate, size=50, font="Lato", color="red", align="top")
temperature = Text(data_box, text=displayTemperature, size=50, font="Lato", color="blue", align="bottom")

app.display()

