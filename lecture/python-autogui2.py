import pyautogui as pg
import webbrowser
import time
import pyperclip
from datetime import datetime

url = 'https://www.google.com'
webbrowser.open(url)
time.sleep(2)

keyword = 'อุณหภูมิกรุงเทพ'
pyperclip.copy(keyword)
time.sleep(1)

pg.hotkey('ctrl','v')
time.sleep(1)

pg.press('enter')
time.sleep(2)

stamp = datetime.now().strftime('%Y-%m-%d %H%M%S')
file = 'capture-{}.png'.format(stamp)
path = 'C:\\Python311\\python101\\pyautogui_capture\\'
pg.screenshot(path+file)
