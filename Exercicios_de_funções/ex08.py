#Crie uma função chamada calculadora que tenha dentro dela outras funções (somar, subtrair, multiplicar, dividir). A função principal deve permitir escolher a operação e retornar o resultado.

def calculadora():
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        if b == 0:
            return "Erro: divisão por zero!"
        return a / b
    
    print("Escolha a operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

    opcao = input("Digite o número da operação: ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        resultado = somar(num1, num2)
    elif opcao == "2":
        resultado = subtrair(num1, num2)
    elif opcao == "3":
        resultado = multiplicar(num1, num2)
    elif opcao == "4":
        resultado = dividir(num1, num2)
    else:
        resultado = "Operação inválida."

    print("Resultado:", resultado)