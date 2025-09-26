#Crie uma classe Usuario com atributos nome e email. Depois, crie uma classe Cliente que herde de Usuario. Crie uma instancia de um cliente e acesse todos os atributos.

# Classe base
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

# Classe Cliente que herda de Usuario
class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)  # chama o construtor da classe Usuario

# Criando uma instância de Cliente
cliente1 = Cliente("Selly Costa", "selly@gmail.com")

# Acessando os atributos
print("Nome do cliente:", cliente1.nome)
print("Email do cliente:", cliente1.email)