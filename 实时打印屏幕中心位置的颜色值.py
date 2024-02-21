import pyautogui
import time

while True:
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2
    color = pyautogui.pixel(center_x, center_y)
    print(f"屏幕中心位置的颜色坐标： ({center_x}, {center_y})，颜色值： {color}")
    time.sleep(1)
