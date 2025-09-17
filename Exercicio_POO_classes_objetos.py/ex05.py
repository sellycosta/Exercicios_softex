# Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione um método depositar(valor) que aumenta o saldo e um método sacar(valor) que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques.

# Definindo a classe ContaBancaria
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print(f"Saque de R${valor:.2f} não permitido. Saldo insuficiente.")

    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo atual: R${self.saldo:.2f}")

# Criando uma conta bancária
conta1 = ContaBancaria("Carlos", 1000.00)

# Exibindo o saldo inicial
conta1.exibir_saldo()

# Realizando um depósito
conta1.depositar(500.00)

# Tentando sacar um valor possível
conta1.sacar(300.00)

# Tentando sacar um valor maior que o saldo
conta1.sacar(1500.00)

# Exibindo o saldo final
conta1.exibir_saldo()