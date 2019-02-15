from microbit import *

rabbit = Image("07070:"
             "07770:"
             "76067:"
             "70607:"
             "07770")
display.show(rabbit)
rabbitFeed1 = Image("00000:"
                "00000:"
                "70000:"
                "77000:"
                "77000:")

rabbitFeed2 = Image("00006:"
                "70000:"
                "77000:"
                "77000:"
                "77000:")

rabbitFeed3 = Image("70000:"
                "77600:"
                "77000:"
                "77000:"
                "70000:")

rabbitFeed4 = Image("00000:"
                "7000:"
                "77000:"
                "77000:"
                "77000:")

rabbitFeed5 = Image("00000:"
                "00000:"
                "70000:"
                "77000:"
                "77000:")


rabbitPlay1 = Image("00000:"
                "00000:"
                "60000:"
                "60000:"
                "06000:")


rabbitFeed = [rabbitFeed1, rabbitFeed2, rabbitFeed3, rabbitFeed4, rabbitFeed5]
rabbitPlay = [rabbitPlay1]
while True:
    if button_a.is_pressed():
        display.show(rabbitFeed, delay = 200)
    elif button_b.is_pressed():
        display.show(rabbitPlay, delay = 300)
    else:
        display.show(rabbit)
