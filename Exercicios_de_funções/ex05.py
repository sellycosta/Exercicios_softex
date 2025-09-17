#Crie uma função chamada operacoes que receba dois números e retorne a soma, a subtração e a multiplicação deles.

def operacoes(numero1, numero2):
    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    return soma, subtracao, multiplicacao

resultado = operacoes(10, 5)

print("Soma:", resultado[0])
print("Subtração:", resultado[1])
print("Multiplicação:", resultado[2])