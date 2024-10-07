import pyautogui
import time
import keyboard
import easyocr
import cv2
import numpy
import torch

print("CUDA available: ", torch.cuda.is_available())
print("Device count: ", torch.cuda.device_count())
print("Current device: ", torch.cuda.current_device())
print("Device name: ", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU")

start_stop_hotkey = "f6"
quit_hotkey = "f9"

program_start_time = time.time()

reader = easyocr.Reader(["en"], gpu=True)
active = False
processed_image_count = 0
fish_caught = 0

def proccess_screen():
    global fish_caught, processed_image_count
    screen_width, screen_height = pyautogui.size()
    screenshot_region = (
    int(3/4 * screen_width),  # left
    int(3/4 * screen_height), # top
    int(1/4 * screen_width),  # width
    int(1/4 * screen_height)  # height
    )

    screenshot = pyautogui.screenshot(region=screenshot_region) # Capture Screenshot
    processed_image = cv2.cvtColor(numpy.array(screenshot),cv2.COLOR_RGB2BGR)
    processed_image_count += 1
    words = reader.readtext(processed_image)
    for word in words:
            if "fishing bobber" in word[1].lower():
                fish_caught += 1
                print(fish_caught, "items caught")
                pyautogui.rightClick()
                time.sleep(3)
                pyautogui.rightClick()
                break

while True:
    if keyboard.is_pressed(start_stop_hotkey):
        print (start_stop_hotkey,"was pressed!")
        active = not active
        time.sleep(0.5)
    if keyboard.is_pressed(quit_hotkey):
        print(quit_hotkey,"was pressed!")
        print("Quitting in 3!")
        print(processed_image_count, "processed images")
        elapsed_time = time.time() - program_start_time
        print(f"Program ran for {elapsed_time:.2f} seconds.")
        time.sleep(1)
        print("2!")
        time.sleep(1)
        print("1!")
        time.sleep(1)
        quit()
    if active:
        time.sleep(.75)
        proccess_screen()


