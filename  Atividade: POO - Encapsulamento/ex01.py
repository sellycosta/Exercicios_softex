#Na classe, ContaBancaria, converta saldo para uma atributo privado. Crie um método setter e um getter para acessar e modificar essa atributo, seguindo uma regra lógica (Ex: saldo não pode ser negativo)

class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # saldo é agora um atributo privado

    # Método getter para acessar o saldo
    def get_saldo(self):
        return self.__saldo

    # Método setter para modificar o saldo (com regra: saldo não pode ser negativo)
    def set_saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print("Erro: o saldo não pode ser negativo.")

