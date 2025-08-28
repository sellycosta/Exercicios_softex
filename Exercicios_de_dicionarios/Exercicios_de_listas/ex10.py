#10- Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:#
#notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.#

notas = []
aluno1 = []
aluno1.append(float(input("Digite a primeira nota do aluno 1: ")))
aluno1.append(float(input("Digite a segunda nota do aluno 1: ")))
aluno1.append(float(input("Digite a terceira nota do aluno 1: ")))
notas.append(aluno1)

aluno2 = []
aluno2.append(float(input("Digite a primeira nota do aluno 2: ")))
aluno2.append(float(input("Digite a segunda nota do aluno 2: ")))
aluno2.append(float(input("Digite a terceira nota do aluno 2: ")))
notas.append(aluno2)

media1 = sum(notas[0]) / len(notas[0])
media2 = sum(notas[1]) / len(notas[1])

print("Média do aluno 1:", media1)
print("Média do aluno 2:", media2)