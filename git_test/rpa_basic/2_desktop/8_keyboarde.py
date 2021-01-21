import pyautogui
w= pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

# pyautogui.write("12345")
# pyautogui.write("Nadocoding", interval=0.25)
# pyautogui.write("나도코딩")

# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"],interval=1)

#특수문자
# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

#조합키
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

#간편한 조합키
# pyautogui.hotkey("ctrl","alt","shift","a")
# pyautogui.hotkey("ctrl","a")

import pyperclip
# pyperclip.copy("나도코딩")
# pyautogui.hotkey("ctrl","v")

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

my_write("나도코딩")