import time
import pyautogui

with open('code.txt', 'r') as f:
    time.sleep(5)
    for i in f:
        pyautogui.write(i)
