#Crie uma classe Funcionario que herda de Usuario e, em seguida, crie uma classe Gerente que herda de Funcionario. Mostre como instanciar um gerente e acessar seus atributos.

# Classe base
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

# Classe Funcionario que herda de Usuario
class Funcionario(Usuario):
    def __init__(self, nome, email, cargo):
        super().__init__(nome, email)
        self.cargo = cargo

# Classe Gerente que herda de Funcionario
class Gerente(Funcionario):
    def __init__(self, nome, email, cargo, departamento):
        super().__init__(nome, email, cargo)
        self.departamento = departamento