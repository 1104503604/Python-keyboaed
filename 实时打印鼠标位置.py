import pyautogui
import time

while True:
    x, y = pyautogui.position()
    print(f"鼠标位置： ({x}, {y})")
    time.sleep(1)  # 每隔1秒打印一次鼠标位置
