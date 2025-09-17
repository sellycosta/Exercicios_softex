# Crie uma classe Aluno com atributos nome e nota. Depois crie uma classe Turma que tenha uma lista de alunos e um método adicionar_aluno(aluno). Crie alguns objetos Aluno e adicione-os à turma.

# Classe Aluno
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

# Classe Turma
class Turma:
    def __init__(self):
        self.alunos = []  # Lista vazia de alunos

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        print(f"Aluno {aluno.nome} adicionado com nota {aluno.nota}.")

    def listar_alunos(self):
        print("\nAlunos na turma:")
        for aluno in self.alunos:
            print(f"- {aluno.nome}, Nota: {aluno.nota}")

# Criando objetos da classe Aluno
aluno1 = Aluno("Ana", 8.5)
aluno2 = Aluno("Bruno", 7.0)
aluno3 = Aluno("Carla", 9.2)

# Criando um objeto da classe Turma
turma = Turma()

# Adicionando os alunos à turma
turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)
turma.adicionar_aluno(aluno3)

# Listando os alunos da turma
turma.listar_alunos()