#1- Crie uma classe chamada Pessoa que tenha os atributos nome e idade. Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.

class Pessoa:
    nome= "Fabiana"   
    idade= 35

terreste= Pessoa()
print(Pessoa)

#2- Expanda a classe Pessoa para incluir um método apresentar() que imprima uma frase como:"Olá, meu nome é João e tenho 25 anos.". Teste o método chamando-o a partir de um objeto.

class Pessoa:
    def __init__(self, nome):
        self.nome = Fabiana
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho 35 anos.") 
    pessoa1= Pessoa ("Fabiana")
    pessoa1.apresentar()

