import pyautogui
import time

while True:
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2
    color = pyautogui.pixel(center_x, center_y)
    
    if color == (255, 255, 255):
        print("白色")
    elif color == (0, 0, 0):
        print("黑色")
    
    time.sleep(1)
