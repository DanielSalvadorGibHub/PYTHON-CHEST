import pyautogui as pi

img = pi.locateCenterOnScreen("conectar.png")
img5 = pi.locateCenterOnScreen("top.png")
img2 = pi.locateCenterOnScreen("adicionar.png")
img3 =  pi.locateCenterOnScreen("enviar.png")
img4 = pi.locateCenterOnScreen("avancar.png")



pi.alert("posso começar?")
for repeticao in range(5):
    if img:
        pi.click(x=924, y=105, duration = 1)
        pi.click(img)
        pi.PAUSE = 2.0
        pi.click(img5)
        pi.PAUSE = 2.0
        pi.click(img2)
        pi.PAUSE = 2.0
        pi.write("Olá, vi seu perfil no LinkedIn e gostaria de me conectar com você. Acredito que nossas redes profissionais podem se beneficiar mutuamente e eu adoraria ter a oportunidade de compartilhar ideias e conhecimentos com você.")
        pi.PAUSE = 2.0
        pi.click(img3)

    else:
        pi.click(x=924, y=105)
        pi.keyDown("pagedown")
        pi.click(img4)         
