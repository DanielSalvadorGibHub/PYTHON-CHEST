#ATIVIDADE PRATICA-04

#01-DETERMINAÇÃO DO LOOP:
loop = True
#02-INICIO DO LOOP:
while loop == True:
    #03-APRESENTAÇÃO DAS VARIAVEIS:
    nome = str(input("-Digite o nome do paciente: "))
    idade = int(input("-Digite a idade do paciente(coloque ponto e não virgula): "))
    altura = float(input("-Digite a altura do paciente(coloque ponto e não virgula)"))
    peso = float(input("-Digite o peso do paciente: "))
    #04-CALCULO DO IMC DO PACIENTE?
    imc = (peso/(altura*altura))
    #05-IMC RELACIONADO A CONDICIONAL (MUITO-MARGO):
    if imc <= 0 and imc < 19:
        resultado = "MUITO-MAGRO"
        regime = "Não"
        loop = False
    #06-IMC RELACIONADO A CONDICIONAL (NORMAL):
    elif imc >= 19 and imc < 25:
        resultado = "NORMAL"
        regime = "Não"
        loop = False
    #07-IMC RELACIONADO A CONDICIONAL (SOBREPESO):
    elif imc >= 25 and imc < 30:
        resultado = "SOBREPESO"
        regime = "Sim"
        loop = False
    #08-IMC RELACIONADO A CONDICIONAL (OBESO):
    elif imc >= 30 and imc < 40:
        resultado = "OBESO"
        regime = "Sim"
        loop = False
    #09-IMC RELACIONADO A CONDICIONAL (OBESIDADE-GRAVE):
    elif imc >= 40:
        resultado = "OBESIDADE-GRAVE"
        regime = "Sim"
        loop = False
#10-APRESENTAÇÃO DOS RESULTADOS:
print("="*12)
print(f"-Nome do Paciente: {nome}")
print(f"-Idade do Paciente: {idade}")
print(f"-Altura do Paciente: {altura}")
print(f"-Peso do Paciente: {peso}")
print(f"-IMC do Paciente: {imc:.2f}")
print(f"-Resultado do Exame: {resultado}")
print(f"-Recomendações de regime: {regime}")
print(f"="*12)
#11-DESCISÃO DE REPITIR O EXAME:
repetir = str(input("-Gostaria de examinar outro paciente(sim/não)?"))
if repetir == "sim":
    loop = True
#11-FINALIZAÇÃO DO PROGRAMA:
else:
    print("Fim do programa")
