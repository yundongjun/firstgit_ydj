import pyautogui

# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# for i in pyautogui.locateOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i)

# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)
# pyautogui.click(trash_icon)

# 1.속도 개선
# trash_icon = pyautogui.locateOnScreen("trash_icon.png",grayscale=True)
# pyautogui.moveTo(trash_icon)

# 2.범위 지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png",region=(x,y,width,height))
# pyautogui.moveTo(trash_icon)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png",region=(1012,171,1012-628,375-171))
# pyautogui.moveTo(trash_icon)

# 3.정확도 조정
# file_menu = pyautogui.locateOnScreen("file_menu.png",confidence=0.6)
# pyautogui.moveTo(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png",confidence=0.9)
# pyautogui.moveTo(trash_icon)

# run_btn = pyautogui.locateOnScreen("num_btn.png",confidence=0.9)
# pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우

# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견실패")


import time
import sys

timeout = 10
start = time.time()
file_menu_notepad = None
while file_menu_notepad is None:
    file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepade.png")
    end = time.time()
    if end - start > timeout:
        print("시간종료")
        sys.exit()

pyautogui.click(file_menu_notepad)