#!/usr/bin/python

#Nick - this will keep looping, move mouse all the way to top left or bottom right corner to cancel

while True:

    import pyautogui
    import random

    #Nick - Use this to see how big your screen is

    screensize = pyautogui.size()
    print(screensize)

    #Nick - random variables for movement

    a = random.randint(0,1920)
    b = random.randint(0,1920)

    #Nick - first mouse movement

    pyautogui.moveRel((a), (b), duration=0.5)

    #Nick - second mouse movement

    pyautogui.moveRel(-(a), -(b), duration=0.5)

    #Nick - Cheeky click

    pyautogui.click(clicks=5, interval=0.2, button='left')

    #Nick - Cheeky scroll

    pyautogui.scroll(500)

    #Nick - Cheeky keypress

    pyautogui.typewrite(['up'], interval=2)
