#Contando frequência de palavras
#Escreva uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra.
#palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

def contar_palavras(lista):
    contagem = {}
    for palavra in lista:
        if palavra in contagem:
            contagem[palavra] = contagem[palavra] + 1
        else:
            contagem[palavra] = 1
    return contagem

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

resultado = contar_palavras(palavras)
print(resultado)