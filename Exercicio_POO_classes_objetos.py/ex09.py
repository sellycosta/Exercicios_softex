# Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" e atributos de instância nome e idade. Mostre a diferença entre acessar especie pelo objeto e pela classe.

# Definindo a classe Cachorro
class Cachorro:
    especie = "Canis familiaris"  # Atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome           # Atributo de instância
        self.idade = idade         # Atributo de instância

# Criando um objeto da classe Cachorro
cachorro1 = Cachorro("Rex", 5)

# Acessando o atributo de classe pela CLASSE
print("Acessando pela classe:")
print(Cachorro.especie)

# Acessando o atributo de classe pelo OBJETO
print("\nAcessando pelo objeto:")
print(cachorro1.especie)

# Acessando os atributos de instância
print("\nAtributos de instância:")
print(f"Nome: {cachorro1.nome}")
print(f"Idade: {cachorro1.idade}")