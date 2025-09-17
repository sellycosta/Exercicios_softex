#Crie uma exceção personalizada chamada IdadeInvalidaError. Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa.

class IdadeInvalidaError(Exception):
    pass

def cadastrar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError("Idade não pode ser negativa.")
    print(f"Idade {idade} cadastrada com sucesso!")