#Crie uma classe Carro com os atributos marca, modelo e ano. Use o método __init__ para inicializar esses valores. Crie três objetos e mostre suas informações.

# Definindo a classe Carro
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    # Método para exibir as informações do carro
    def exibir_informacoes(self):
        print(f"Carro: {self.marca} {self.modelo} - Ano: {self.ano}")

# Criando três objetos da classe Carro
carro1 = Carro("Fiat", "Uno", 2020)
carro2 = Carro("Volkswagen", "Gol", 2018)
carro3 = Carro("Chevrolet", "Onix", 2022)

# Exibindo as informações de cada carro
carro1.exibir_informacoes()
carro2.exibir_informacoes()
carro3.exibir_informacoes()