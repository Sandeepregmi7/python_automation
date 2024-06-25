import time
import pyautogui

def great(name):
    greating_message= f"hello ,{name} namaste"
    return greating_message
    
my_guest=['sam','leo','dev','sandip']
for i in my_guest:
    greating_message=great(i)
    time.sleep(3)
    pyautogui.write(greating_message)
    pyautogui.press("enter")