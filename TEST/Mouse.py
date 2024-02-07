import pyautogui
import time
from pynput import mouse

def on_click(x, y, button, pressed):
    if button == mouse.Button.middle and pressed:
        pyautogui.keyDown('win')
        time.sleep(2)
        pyautogui.keyUp('win')
        pyautogui.write('chrome')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.hotkey('ctrl','e')
        pyautogui.write('Test')
        pyautogui.press('enter')


with mouse.Listener(on_click=on_click) as listener:
    listener.join()