import numpy
lista = ['pedra', 'papel', 'tesoura']
elemento = numpy.random.choice(lista)
resultado = False
print("VAMOS JOGAR UM JOGO, escolha entre pedra, papel ou tesoura: ")
while resultado == False:
    escolha = str(input("Escolha um elemento da lista: "))
    if escolha != elemento:
        if elemento == "pedra" and escolha == "papel":
            print(f"O elemento escolhido foi {elemento} e a sua escolha foi {escolha}, você GANHOU!")
            resultado = False
        else:
            print(f"O elemento escolhido foi {elemento} e a sua escolha foi {escolha}, você PERDEU!")

    else:
        print("Deu empate")
