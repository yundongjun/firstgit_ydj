import sys
import pyautogui
import pyperclip

pyautogui.hotkey("win","r")
pyautogui.write("mspaint")
pyautogui.press("enter")

pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]
if window.isMaximized == False:
    window.maximize()

btn_text = pyautogui.locateOnScreen("btn_text.png")

if btn_text:
    pyautogui.click(btn_text,duration=0.5)
else:
    print("찾기 실패")
    sys.exit()

pyautogui.click(200,200,duration=0.5)

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

my_write("참 잘했어요")

pyautogui.sleep(5)

window.close()
pyautogui.sleep(0.5)
pyautogui.press("n")