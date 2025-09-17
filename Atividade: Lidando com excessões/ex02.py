#Peça ao usuário dois números e tente multiplicá-los. Se o usuário digitar algo inválido, exiba uma mensagem de erro.

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")
except ValueError:
    print("Erro: você digitou um valor inválido. Por favor, digite apenas números.")