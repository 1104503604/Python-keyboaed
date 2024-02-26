import pyautogui
import keyboard
press_count = 0

def enter_key():
    global press_count
    # 将鼠标移动到指定位置 (x, y)
    x, y = 1396, 512
    pyautogui.moveTo(x, y)

    # 在当前位置点击鼠标左键
    pyautogui.click()

    pyautogui.moveTo(1, 1)

    press_count = 0

keyboard.add_hotkey('right', enter_key)

def enter_key_1():
    global press_count
    if press_count > 24 :
        enter_key()
    else:
        # 将鼠标移动到指定位置 (x, y)
        x, y = 1327, 504
        pyautogui.moveTo(x, y)

        # 在当前位置点击鼠标左键
        pyautogui.click()

        pyautogui.moveTo(1, 1)
                
        press_count += 1
        print(f"朗读了 {press_count} 次")

keyboard.add_hotkey('down', enter_key_1)

def enter_key_2():
        # 将鼠标移动到指定位置 (x, y)
        x, y = 279, 919
        pyautogui.moveTo(x, y)

        # 在当前位置点击鼠标左键
        pyautogui.doubleClick()

        pyautogui.moveTo(1, 1)
        

keyboard.add_hotkey('ctrl+f', enter_key_2)

def enter_key_3 ():
    global press_count
    # 将鼠标移动到指定位置 (x, y)
    x, y = 1265, 509
    pyautogui.moveTo(x, y)

    # 在当前位置点击鼠标左键
    pyautogui.click()

    pyautogui.moveTo(1, 1)

    press_count = 0

keyboard.add_hotkey('left', enter_key_3 )

def enter_key_4 ():
    global press_count
    # 将鼠标移动到指定位置 (x, y)
    x, y = 1461, 509
    pyautogui.moveTo(x, y)

    # 在当前位置点击鼠标左键
    pyautogui.click()

keyboard.add_hotkey('1', enter_key_4 )

def enter_key_5 ():
    global press_count
    # 将鼠标移动到指定位置 (x, y)
    x, y = 1727, 501
    pyautogui.moveTo(x, y)

    # 在当前位置点击鼠标左键
    pyautogui.click()

    press_count = 0

keyboard.add_hotkey('3', enter_key_5 )

# 开始主循环，等待用户输入 
keyboard.wait()
