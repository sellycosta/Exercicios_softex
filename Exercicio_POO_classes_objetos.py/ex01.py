#1- Crie uma classe chamada Pessoa que tenha os atributos nome e idade. Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

print("Nome:", pessoa1.nome, "Idade:", pessoa1.idade)
print("Nome:", pessoa2.nome, "Idade:", pessoa2.idade)

