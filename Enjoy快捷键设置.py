import keyboard
import pyautogui

def enter_key():
    # 将鼠标移动到指定位置 (x, y)
    x, y = 1429, 511
    pyautogui.moveTo(x, y)

    # 在当前位置点击鼠标左键
    pyautogui.click()

    keyboard.press('space')
    keyboard.release('space')

keyboard.add_hotkey('right', enter_key)

def enter_key_1():
    keyboard.press('space')
    keyboard.release('space')

keyboard.add_hotkey('down', enter_key_1)

def enter_key_2 ():
    # 将鼠标移动到指定位置 (x, y)
    x, y = 3231, 276
    pyautogui.moveTo(x, y)

    # 模拟鼠标滚轮向上滚动
    pyautogui.scroll(10000)

    # 在当前位置点击鼠标左键
    pyautogui.click()
    
    keyboard.press('space')
    keyboard.release('space')

keyboard.add_hotkey('up', enter_key_2 )

def enter_key_3 ():
    # 将鼠标移动到指定位置 (x, y)
    x, y = 1295, 500
    pyautogui.moveTo(x, y)

    # 在当前位置点击鼠标左键
    pyautogui.click()
    
    keyboard.press('space')
    keyboard.release('space')

def enter_key_4 ():
    # 将鼠标移动到指定位置 (x, y)
    x, y = 1622, 1955
    pyautogui.moveTo(x, y)

    # 在当前位置点击鼠标左键
    pyautogui.click()

keyboard.add_hotkey('0', enter_key_4 )


keyboard.wait()

