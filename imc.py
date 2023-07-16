from time import sleep

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
def mensagem_imc():
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"
    
print('Olá sejá bem-vindo ao seu atendimento médico: ')

while True:
    option=int(input(' 1: CALCULAR IMC  2: CANCELAR ATENDIMENTO: '))
    if option == 1:
        nome=input("Qual é seu nome: ")
        peso = float(input("Digite o seu peso em kg: "))
        altura = float(input("Digite a sua altura em metros: "))
        imc = calcular_imc(peso, altura)
        msg= mensagem_imc()
        print(f"Olá {nome}, seu IMC é: {imc:.2f}, {msg}")
        sleep(1)
    else:
        print("Tchau, tenha um otimo dia, espero que tenha gostado do nosso atendimento!!")
        break