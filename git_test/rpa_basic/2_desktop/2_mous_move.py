import pyautogui

# pyautogui.moveTo(200,100)
# pyautogui.moveTo(100,200,duration=5)

# pyautogui.moveTo(100,100,duration=1)
# pyautogui.moveTo(200,200,duration=1)
# pyautogui.moveTo(300,300,duration=1)

# pyautogui.move(100,100,duration=1)
# print(pyautogui.position())

p = pyautogui.position()
print(p[0],p[1])
print(p.x,p.y)