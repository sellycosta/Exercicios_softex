#Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use:
#try para a conversão,
#else para verificar se é par ou ímpar,
#finally para exibir "Fim do programa".

try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: Você não digitou um número inteiro válido.")
else:
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
finally:
    print("Fim do programa.")