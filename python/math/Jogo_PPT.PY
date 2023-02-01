from random import randint
from time import sleep
resultado = False
lista = ['PEDRA', 'PAPEL', 'TESOURA']
print("="*12)
print("ESCOLHGA ENTRE:")
sleep(1)
print("[0]-Pedra")
sleep(1)
print("[1]-Papel")
sleep(1)
print("[2]-Tesoura")
sleep(1)
print("="*12)
while resultado == False:
    sorte = randint(0,2)
    jogada = int(input("Qual vai ser a sua jogada?  "))
    sleep(0.5)
    print("="*12)
    sleep(0.5)
    print("JO")
    sleep(0.5)
    print("KEN")
    sleep(0.5)
    print("PO")
    sleep(0.5)
    print("="*12)
    print(f"ADVERSARIO JOGOU: {lista[sorte]}!")
    print(f"VOCÊ JOGOU: {lista[jogada]}!")
    print("="*12)
    if sorte == 0: #PEDRA
        if jogada == 0:
            print("EMPATE")
        elif jogada == 1:
            print("JOGADOR VENCEU!")
            resultado = True
        elif jogada ==2:
            print("ADVERSARIO VENCEU!")

    if sorte == 1: #PAPEL
        if jogada == 0:
            print("ADVERSARIO VENCEU!")
        elif jogada == 1:
            print("EMPATE")
        elif jogada ==2:
            print("JOGADOR VENCEU!")
            resultado = True

    if sorte == 2: #TESOURA
        if jogada == 0:
            print("ADVERSARIO VENCEU!")
        elif jogada == 1:
            print("JOGADOR VENCEU!")
            resultado = True
        elif jogada == 2:
            print("EMPATE")
print("Acabou!")
