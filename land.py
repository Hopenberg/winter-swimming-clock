from random import randint
import time
from guizero import App, Text, TextBox, PushButton, Slider, Picture, Box
import bluetooth

TIME_UNIT = 1000

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

def readHeartrate():
    target_device_address = "00:11:22:33:44:55" 
    port = 1 

    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((target_device_address, port))

    data = sock.recv(1024)

    heartrateFromWater = data.split("#--#")[0]

    heartrate.value = randint(80,140)

def readTemperature():
    target_device_address = "00:11:22:33:44:55"  
    port = 1  

    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((target_device_address, port))

    data = sock.recv(1024)

    tempreatureFromWater = data.split("#--#")[1]

    temperature.value = randint(10,30)



app = App(title="Winter swimming clock", width=1024, height=600)

displayClock = "00:00"
displayHeartrateValue = "123 <3"
displayTemperatureValue = "23 C"
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

heartrate = Text(data_box, text=displayHeartrateValue, size=50, font="Lato", color="red", align="top")
temperature = Text(data_box, text=displayTemperatureValue, size=50, font="Lato", color="blue", align="bottom")

temperature.repeat(TIME_UNIT, readTemperature)
heartrate.repeat(TIME_UNIT, readHeartrate)


app.display()

