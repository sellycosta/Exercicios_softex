#Crie uma função chamada media que receba uma quantidade variável de números e retorne a média deles. Teste com 3, 5 e 7 valores diferentes.

def media(*numeros):
    total = sum(numeros)
    quantidade = len(numeros)
    return total / quantidade
print("Média de 3 valores:", media(10, 20, 30))

print("Média de 5 valores:", media(5, 10, 15, 20, 25))

print("Média de 7 valores:", media(1, 2, 3, 4, 5, 6, 7))