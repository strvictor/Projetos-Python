from playsound import playsound
import pyautogui
def toca(caminho):
    for c in range(0, 50):
        pyautogui.press('volumeup')
    playsound(f'{caminho}')