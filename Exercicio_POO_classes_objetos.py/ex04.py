# Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos (por exemplo, mudar o ano). Imprima antes e depois da alteração.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    # Método para exibir as informações do carro
    def exibir_informacoes(self):
        print(f"Carro: {self.marca} {self.modelo} - Ano: {self.ano}")

# Criando um objeto da classe Carro
carro1 = Carro("Toyota", "Corolla", 2020)

# Exibindo as informações do carro antes da alteração
print("Antes da alteração:")
carro1.exibir_informacoes()

# Alterando o valor do atributo 'ano'
carro1.ano = 2023

# Exibindo as informações do carro depois da alteração
print("\nDepois da alteração:")
carro1.exibir_informacoes()