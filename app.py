import pyautogui
from time import sleep

pyautogui.click(957,540, duration=2)
pyautogui.write('eduardo perucci')

pyautogui.click(960,568, duration=2)
pyautogui.write('senha123')

pyautogui.click(868,595, duration=2)


with open('registros.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        
        pyautogui.click(1034,845, duration=2)
        pyautogui.write(produto)
        
        pyautogui.click(1222,710, duration=2)
        pyautogui.write(quantidade)
        
        pyautogui.click(976,509, duration=2)
        pyautogui.write(preco)
        
        pyautogui.click(868,595, duration=1)
        sleep(1)