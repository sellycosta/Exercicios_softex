#Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro:

#ValueError se o usuário digitar algo inválido
#ZeroDivisionError se tentar dividir por zero

try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    resultado = a / b
    print(f"Resultado da divisão: {resultado}")

except ValueError:
    print("Erro: Você digitou um valor inválido. Digite apenas números.")

except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")