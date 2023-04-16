print("CALCULADORA SIMPLES EM PYTHON")

sair = False
while sair == False:

    valor1 = input("Digite o primeiro numero: ")
    valor1 = int(valor1)
    operador = input("Digite o operador (+-/*): ")
    valor2 = input("Digite o segundo numero: ")
    valor2 = int(valor2)

#operacao de soma   
    if operador == "+":
        operacao = valor1 + valor2

#operacao de subtracao       
    if operador == "-":
        operacao = valor1 - valor2

#operacao de divisao           
    if operador == "/":
        operacao = valor1 / valor2

#operacao de multiplicacao           
    if operador == "*":
        operacao = valor1 * valor2

    print("Resultado: ")
    print(operacao)

    teste = input("Deseja sair (n/s): ")

    if teste == "s":

        sair = True
