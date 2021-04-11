import pyautogui as auto
import time as t


def link():
    abrir()
    for i in range(3):
        eleccion(i)

    
def abrir():
    auto.press("win")
    t.sleep(2)
    auto.write("edge")
    auto.press("enter")
    t.sleep(3)
    auto.hotkey("ctrl","N")
    t.sleep(3)
    auto.write("https://juniorguerra.github.io/ProgramAnuncios/")
    t.sleep(3)
    auto.press("enter")

def eleccion(num):

    if num == 0:
        auto.press("tab")
        auto.press("enter")
        num = 1
        cambio()
        abrir
    elif num == 1:
        auto.press('tab')
        auto.press('tab')
        auto.press('enter')
        num = 2
        cambio()
        abrir()
    elif num == 2:
        auto.press('tab')
        auto.press('tab')
        auto.press('tab')
        auto.press('enter')
        cambio()
        abrir()

def cambio():
    auto.hotkey('alt','F4')

link()
