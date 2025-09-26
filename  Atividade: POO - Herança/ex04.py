#Na classe Cliente, adicione o atributo saldo. Adicione um método construtor em Cliente que inicialize também os atributos de Usuario usando super().

# Classe base
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def saudacao(self):
        return "Olá, usuário"

# Classe derivada
class Cliente(Usuario):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)  # Chama o construtor da classe Usuario
        self.saldo = saldo             # Atributo exclusivo de Cliente

    def saudacao(self):
        return "Olá, cliente"

        