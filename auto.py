import pyautogui
from time import sleep

# 雙頁

# acer 21:9
# x1 = 0
# x2 = 1440
# y1 = 749
# y2 = 2691

#areo oled
x1 = 0
x2 = 2160
y1 = 462
y2 = 3379

start=1
end=
file_name=''

sleep(5)
for i in range(start, end):
    myScreenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
    myScreenshot.save(f'{file_name} {i:03d}.png')
#     sleep(0.5)
    pyautogui.press('right')
    sleep(1.5)

# 雙頁切半

# x1 = 640
# x2 = 2800
# y1 = 0
# y2 = 1440
# sleep(3)
# for i in range(-2,180):
#     if not (i % 2) : # 左半
#         myScreenshot = pyautogui.screenshot(region=(x1, y1, (x2-x1)/2, y2-y1))
#         myScreenshot.save(f'./透視入門聖經 {i:03d}.png')
#         sleep(0.5)
#     else :           # 右半
#         myScreenshot = pyautogui.screenshot(region=(x1+(x2-x1)/2, y1, (x2-x1)/2, y2-y1))
#         myScreenshot.save(f'./透視入門聖經 {i:03d}.png')
#         sleep(0.5)
#         pyautogui.press('right')
#         sleep(2)