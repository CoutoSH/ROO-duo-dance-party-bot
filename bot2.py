from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

time.sleep(1)
confidence_level = 0.4  # Lower confidence level for better matching
file_path = 'bot4.png'
region1 = (870, 490, 820, 500)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while not keyboard.is_pressed('q'):
    try:
        location = pyautogui.locateOnScreen(file_path, region=region1, confidence=confidence_level)
    except pyautogui.ImageNotFoundException:
        location = None
        
    if location is not None:
        x, y, _, _ = location
        time.sleep(0.3)
        click(x+60, y+60)  # Adjust click coordinates based on region
        time.sleep(0.01)
        print("click")
        # Optionally, remove break if you want to continue clicking whenever the image is found

    #time.sleep(1)  # Adjust sleep time as needed to control the frequency of checks

print("Exiting script...")
