import pyautogui
import keyboard

def enter_key():
    # 将鼠标移动到指定位置 (x, y)
    x, y = 1429, 511
    pyautogui.moveTo(x, y)

    # 在当前位置点击鼠标左键
    pyautogui.click()

    keyboard.press('space')
    keyboard.release('space')

    # 将鼠标往下移动，不要遮住单词
    pyautogui.moveTo(x, y + 130)

keyboard.add_hotkey('right', enter_key)

def enter_key_1():
    keyboard.press('space')
    keyboard.release('space')

keyboard.add_hotkey('down', enter_key_1)

def enter_key_2 ():
    # 将鼠标移动到指定位置 (x, y)
    x, y = 3231, 229
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

    # 将鼠标往下移动，不要遮住单词
    pyautogui.moveTo(x, y + 130)

keyboard.add_hotkey('left', enter_key_3 )

def enter_key_4 ():
    # 将鼠标移动到指定位置 (x, y)
    x, y = 1495, 501
    pyautogui.moveTo(x, y)

    # 在当前位置点击鼠标左键
    pyautogui.click()

    # 将鼠标往下移动，不要遮住单词
    pyautogui.moveTo(x, y + 130)

keyboard.add_hotkey('1', enter_key_4 )

def enter_key_5 ():
    # 将鼠标移动到指定位置 (x, y)
    x, y = 1759, 501
    pyautogui.moveTo(x, y)

    # 在当前位置点击鼠标左键
    pyautogui.click()

    # 将鼠标往下移动，不要遮住单词
    pyautogui.moveTo(x, y + 130)

keyboard.add_hotkey('3', enter_key_5 )

# 开始主循环，等待用户输入 
keyboard.wait()

