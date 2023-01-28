import random
quest = str(input("Gostaria de jogar o dado? "))
valor = random.randint(1,20)
if quest == "sim":
    if valor < 9:
        print(f"poxa, o resultado dos dados foi {valor}.")
    if valor > 10:
        print(f"Uau, o valor dado foi {valor} ")        
else:
    print("Desculpe não vou rolar os dados")
