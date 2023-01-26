import pyautogui 

#imagens que você deseja pesquisar e inpu para digitar algo onde o python vai puscar o que voc~e pesquisou no google:
img = pyautogui.locateCenterOnScreen('img.png')
img2 = pyautogui.locateCenterOnScreen('img2.png')
var1 = str(input("O que você quer pesquisar?"))

#alera e execução do código:
pyautogui.alert("Apartir desse momento o seu mouse e teclado vão ser controlados pelo computador, aguarde")
pyautogui.click(img, duration = 1)
pyautogui.click(x=787, y=420, duration = 1)                           
pyautogui.write(var1)
pyautogui.press("enter")
