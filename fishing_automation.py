import pyautogui
import time
import keyboard
import easyocr
import cv2
import numpy

start_stop_hotkey = "f6"
quit_hotkey = "f9"
screen_width, screen_height = pyautogui.size()
screenshot_region = (0, int(screen_height * 3 / 4), screen_width, int(screen_height / 4))

reader = easyocr.Reader(["en"], gpu=True)
active = False
    

while True:
    if keyboard.is_pressed(start_stop_hotkey):
        print (start_stop_hotkey,"was pressed!")
        active = not active
        time.sleep(0.5)
    if keyboard.is_pressed(quit_hotkey):
        print(quit_hotkey,"was pressed!")
        print("Quitting in 3!")
        time.sleep(1)
        print("2!")
        time.sleep(1)
        print("1!")
        time.sleep(1)
        quit()
    if active:
        screenshot = pyautogui.screenshot(region=screenshot_region)
        processed_image = cv2.cvtColor(numpy.array(screenshot),cv2.COLOR_RGB2BGR)
        words = reader.readtext(processed_image)
        for word in words:
            if "fishing bobber" in word[1].lower():
                fish = True
                print("fish found!")
                pyautogui.rightClick()
                time.sleep(.5)
                pyautogui.rightClick()
                break

