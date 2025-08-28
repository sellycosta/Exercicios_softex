#Dicionário com listas
#Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.

alunos = {
    "João": [7, 8, 9],
    "Maria": [6, 9, 8],
    "Pedro": [10, 7, 9]
}
for nome in alunos:
    notas = alunos[nome]
    media = sum(notas) / len(notas)
    print("Média de", nome, ":", media)