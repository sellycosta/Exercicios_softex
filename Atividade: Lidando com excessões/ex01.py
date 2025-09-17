#Escreva um programa que peça ao usuário para digitar um número. Trate o erro caso ele digite algo que não seja um número inteiro.

try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou o número {numero}.")
except ValueError:
    print("Erro: você não digitou um número inteiro válido.")