#Expanda a classe Pessoa para incluir um método apresentar() que imprima uma frase como:"Olá, meu nome é João e tenho 25 anos.". Teste o método chamando-o a partir de um objeto.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    # Método apresentar
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando dois objetos da classe Pessoa
pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

# Chamando o método apresentar
pessoa1.apresentar()
pessoa2.apresentar()