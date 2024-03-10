import webbrowser as web
import pyautogui
import time
import keyboard as k

def sendmessage(number, message):
    web.open(f"https://web.whatsapp.com/send?phone={number}&text={message}")
    time.sleep(20)
    pyautogui.click(1075, 975)
    time.sleep(10)
    k.press_and_release('enter')
