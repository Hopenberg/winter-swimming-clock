import time
from guizero import App, Text, TextBox, PushButton, Slider, Picture

def say_my_name():
    welcome_message.value = my_name.value

def change_text_size(slider_value):
    welcome_message.size = slider_value

def secondsToText(seconds):
    minutes = str(int(seconds / 60))
    secondsPart = str(seconds % 60)

    if len(str(secondsPart)) == 1:
        secondsPart = "0" + secondsPart

    return "0" + minutes + ":" + secondsPart

def textToSeconds(text):
    [minutes, seconds] = text.split(":")
    
    return minutes * 60 + seconds

def incrementTime(timer):
    seconds = textToSeconds(welcome_message.value)
    seconds = int(seconds) + 1
    welcome_message.value = secondsToText(seconds)

app = App(title="Hello world", width=1000)

displayClock = "00:00"
timer = 0

welcome_message = Text(app, text=displayClock, size=40, font="Ariel", color="lightblue")
my_name = TextBox(app, width=30)
update_text = PushButton(app, command=say_my_name, text="Display my name")
text_size = Slider(app, command=change_text_size, start=10, end=80)

welcome_message.repeat(50, incrementTime, args=[timer])

app.display()

