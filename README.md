# Python Mouse Wiggler
Python script created using PyAutoGUI to simulate random mouse and keyboard movements...basically to stop screensavers, your PC going to sleep or to look "always" active at work :-D

## About

This is a quick script for fun and to practice my Python skillz which I've wanted to build for a while.

You can learn the basics of controlling the mouse and keyboard from Automate the Borings Stuff chapter 20 (https://automatetheboringstuff.com/2e/chapter20/), but the example project didn't really do it for me so I decided to build a random mouse/keyboard script which I like to call Mouse Wiggler.

## How to use

Just run the script using terminal or your IDE, and it will loop through until an error occurs.

There are two ways an error might happen:

1. Script accidentally moves the mouse to the top-left hand corner of the screen

2. You manually force the mouse to the top-left hand corner of the screen.

This is a built in failsafe and will automatically create an exception error which stops the script.

## FAQs

**What libraries does your script use?**

Just two pyautogui and random. Both can be installed from PIP/PYPI.

**Do you work somewhere that monitors your mouse movements?**

No...well not that I know of :-D

It's just a bit of fun on a longstanding "joke" about looking busy at work by never going to inactive/away on chat software except for meetings/lunch.

## How

## Further Reading

- Official git of PyAutoGUI https://github.com/asweigart/pyautogui 

- Office Website of PyAutoGUI https://pyautogui.readthedocs.io/en/latest/



