import time
import pyautogui
site = str(input('SUA URL:'))
tempo = int(input('TEMPO PAR ESPERA NA PAGINA:'))
views = int(input('VIEWS:'))
if pyautogui:
    pyautogui.PAUSE = (3)
    pyautogui.press('Win')
    pyautogui.write('GO')
    pyautogui.press('Enter')
    pyautogui.write('{}'.format(site))
    pyautogui.press('Enter')
    for c in range (views):
        time.sleep(tempo)
        pyautogui.hotkey('F5')

    pyautogui.hotkey('Alt', 'F4')
