#Crie uma classe Autenticacao com um método login(). Crie outra classe Permissao com um método verificar_permissao(). Em seguida, crie uma classe Administrador que herda de ambas. Como usar os métodos herdados?

# Classe 1: Autenticacao
class Autenticacao:
    def login(self, usuario, senha):
        # Simulação simples de login
        if usuario == "admin" and senha == "1234":
            print("Login realizado com sucesso.")
        else:
            print("Usuário ou senha incorretos.")

# Classe 2: Permissao
class Permissao:
    def verificar_permissao(self, nivel):
        if nivel == "admin":
            print("Permissão concedida.")
        else:
            print("Permissão negada.")

# Classe 3: Administrador herda das duas
class Administrador(Autenticacao, Permissao):
    def __init__(self, nome):
        self.nome = nome