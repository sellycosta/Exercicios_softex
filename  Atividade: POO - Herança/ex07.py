#Usando o exemplo anterior, adicione um método status() em Autenticacao e também em Permissao. Se a classe Administrador herda das duas, qual versão de status() será chamada? Use Administrador.__mro__ para mostrar a ordem.

# Classe 1: Autenticacao
class Autenticacao:
    def login(self, usuario, senha):
        if usuario == "admin" and senha == "1234":
            print("Login realizado com sucesso.")
        else:
            print("Usuário ou senha incorretos.")

    def status(self):
        print("Status de Autenticação: OK")

# Classe 2: Permissao
class Permissao:
    def verificar_permissao(self, nivel):
        if nivel == "admin":
            print("Permissão concedida.")
        else:
            print("Permissão negada.")

    def status(self):
        print("Status de Permissão: OK")

# Classe 3: Administrador herda de ambas
class Administrador(Autenticacao, Permissao):
    def __init__(self, nome):
        self.nome = nome