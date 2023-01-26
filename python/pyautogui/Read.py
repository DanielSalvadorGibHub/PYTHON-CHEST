with open('lista.txt','r') as arquivo:
            for postes in arquivo:
                ps = postes.split(',')[0]
                pyautogui.doubleClick(x=507, y=307)
                pyautogui.PAUSE = 2.0
                pyautogui.write(ps)
                print(ps, "OK")