import pyautogui
import time
# # open the calculator app first.
# # get the screenshot image of each number button using the following commands 
# position_xy = pyautogui.position() # before running the code, position each number botton of calc with a mouse and get the position coordinate of the cursor.
# pyautogui.screenshot('./../resource/0.png', region=(position_xy.x-20, position_xy.y-20, 40, 40)) # save the number button screenshot image as a 40 X 40 png file.

# # calculate 70 X 21 - 3
# get the position of necessary buttons of cal
num0_xy = pyautogui.locateCenterOnScreen('./../resource/0.png')
num1_xy = pyautogui.locateCenterOnScreen('./../resource/1.png')
num2_xy = pyautogui.locateCenterOnScreen('./../resource/2.png')
num3_xy = pyautogui.locateCenterOnScreen('./../resource/3.png')
num7_xy = pyautogui.locateCenterOnScreen('./../resource/7.png')

equal_xy = pyautogui.locateCenterOnScreen('./../resource/equal.png')
minus_xy = pyautogui.locateCenterOnScreen('./../resource/minus.png')
multiple_xy = pyautogui.locateCenterOnScreen('./../resource/multiple.png')

# calculate the expression
pyautogui.click(num7_xy)
pyautogui.click(num0_xy)
pyautogui.click(multiple_xy)
pyautogui.click(num2_xy)
pyautogui.click(num1_xy)
pyautogui.click(minus_xy)
pyautogui.click(num3_xy)
pyautogui.click(equal_xy)

# plus run this file and have a fun.... (^ _ ^)
