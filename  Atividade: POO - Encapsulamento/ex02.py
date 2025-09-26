#Crie uma classe, Pessoa, que tenha os atributos: nome, data de nascimento, cpf, identidade. Deixe os atributos cpf e identidade como privado e monte os métodos setters e getters para acessar e editar os valores

class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf              # atributo privado
        self.__identidade = identidade  # atributo privado

    # Getter para CPF
    def get_cpf(self):
        return self.__cpf

    # Setter para CPF
    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    # Getter para identidade
    def get_identidade(self):
        return self.__identidade

    # Setter para identidade
    def set_identidade(self, nova_identidade):
        self.__identidade = nova_identidade