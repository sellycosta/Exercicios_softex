#Implemente um método exibir_informacoes() na classe Usuario e herde esse método em Cliente. Mostre como chamar o método herdado a partir de um objeto Cliente.

# Classe base
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    # Método para exibir as informações do usuário
    def exibir_informacoes(self):
        print("Nome:", self.nome)
        print("Email:", self.email)

# Classe Cliente que herda de Usuario
class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)  # chama o construtor da classe Usuario

# Criando uma instância de Cliente
cliente1 = Cliente("Selly Costa", "selly.costa@gmail.com")

# Chamando o método herdado da classe Usuario
cliente1.exibir_informacoes()