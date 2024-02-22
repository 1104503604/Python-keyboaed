import pyautogui
import pynput
import keyboard

print("按下数字1时，启动鼠标监视器")
print("按下数字2时，关闭鼠标监视器")
print("按下数字3时，关闭程序")

# 全局变量以跟踪监听器状态
mouse_listener = None

# 举个例子，移动鼠标
def enter_key():
    # 将鼠标移动到指定位置 (x, y)
    x, y = 1429, 511
    pyautogui.moveTo(x, y, duration=5)  # 设置移动时间为5秒

    # 在当前位置点击鼠标左键
    pyautogui.click()

# 添加一个热键：当按下右箭头键时，执行 enter_key 函数
keyboard.add_hotkey('right', enter_key)

def start_listeners():
    global mouse_listener
    # 创建一个鼠标监听器，禁止鼠标事件
    mouse_listener = pynput.mouse.Listener(suppress=True)
    mouse_listener.start()

def stop_listeners():
    global mouse_listener
    if mouse_listener:
        mouse_listener.stop()

# 定义一个函数，以在按下 1 键时启动监听器
def start_on_1():
    print("启动鼠标监听器")
    start_listeners()

# 定义一个函数，以在按下 2 键时停止监听器
def stop_on_2():
    print("停止鼠标监听器")
    stop_listeners()

# 定义一个函数，以在按下 3 键时退出程序
def exit_on_3():
    print("退出程序")
    stop_listeners()
    # 释放所有热键
    keyboard.unhook_all()
    # 结束主循环
    keyboard.stash_state()

# 最初启动监听器
start_listeners()

# 添加三个热键：1，2，3
keyboard.add_hotkey('1', start_on_1)
keyboard.add_hotkey('2', stop_on_2)
keyboard.add_hotkey('3', exit_on_3)

# 开始主循环，等待用户输入
keyboard.wait()
