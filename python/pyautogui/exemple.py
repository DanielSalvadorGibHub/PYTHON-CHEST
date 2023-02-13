import pyautogui as py

emp = str(input("poderia informar o nome?: "))
qnt = int(input("poderia informar a quantidade?: "))

py.alert("tudo pronto?")

for xxx in range(qnt):
    py.click(x=-1600, y=151)
    py.PAUSE = 3.0
    py.hotkey("ctrl","c")
    py.PAUSE = 3.0
    py.click(img)
    py.hotkey("ctrl","v")
    py.PAUSE = 3.0
    py.click(x=419, y=465)
    py.PAUSE = 3.0            
    py.click(x=493, y=461)
    py.PAUSE = 2.0
    py.click(x=996, y=164)
    py.PAUSE = 2.0  
    py.click(x=1153, y=593)
    py.PAUSE = 3.0
    py.click(x=374, y=439)
    py.PAUSE = 3.0
    py.write(emp)
    py.PAUSE = 3.0
    py.click(x=694, y=618)
    py.PAUSE = 3.0
    py.click(x=529, y=501)
    py.PAUSE = 3.0
    py.click(x=605, y=666)
    py.PAUSE = 3.0
    py.click(514, 496)
    py.PAUSE = 3.0
    py.doubleClick(x=583, y=322)
    py.press("backspace")
    py.PAUSE = 3.0
    py.click(x=-1547, y=317)
    py.PAUSE = 3.0
    py.press("down")
    
py.alert("terminei")
