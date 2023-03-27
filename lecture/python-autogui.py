import time
import pyautogui as pg
import webbrowser

url = 'https://www.google.com'

def autosearch():
    webbrowser.open(url)
    pg.click(752,471)
    time.sleep(1)
    pg.write('cute cat')
    pg.press('enter')
    time.sleep(1)
    pg.click(323,181)

autosearch()
