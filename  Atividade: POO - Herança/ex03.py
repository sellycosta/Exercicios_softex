#Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário". Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente". Mostre como funciona a chamada.

# Classe base
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def saudacao(self):
        return "Olá, usuário"

# Classe derivada
class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)

    # Sobrescrevendo o método saudacao()
    def saudacao(self):
        return "Olá, cliente"

# Criando instâncias
usuario1 = Usuario("Selly", "selly@email.com")
cliente1 = Cliente("Isabel", "isabel@email.com")

# Chamando os métodos
print(usuario1.saudacao())  # Saída: Olá, usuário
print(cliente1.saudacao())  # Saída: Olá, cliente
