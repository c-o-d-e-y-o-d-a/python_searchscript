import pyautogui
import time


time.sleep(9)

for line in open("./fd.txt","r"):
    pyautogui.typewrite(line)
    pyautogui.press("enter")
    time.sleep(1)