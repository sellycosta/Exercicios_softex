# Modifique a classe ContaBancaria para que o método sacar retorne True se a operação for bem-sucedida e False caso contrário. Teste o retorno e imprima mensagens adequadas.

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
            return True  # Saque realizado com sucesso
        else:
            return False  # Saldo insuficiente

    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo atual: R${self.saldo:.2f}")

# Criando uma conta
conta1 = ContaBancaria("Carlos", 1000.00)

# Exibindo saldo inicial
conta1.exibir_saldo()

# Fazendo um depósito
conta1.depositar(500.00)

# Tentando sacar um valor que está disponível
valor_saque1 = 300.00
if conta1.sacar(valor_saque1):
    print(f"Saque de R${valor_saque1:.2f} realizado com sucesso.")
else:
    print(f"Não foi possível sacar R${valor_saque1:.2f}: saldo insuficiente.")

# Tentando sacar um valor maior do que o saldo
valor_saque2 = 2000.00
if conta1.sacar(valor_saque2):
    print(f"Saque de R${valor_saque2:.2f} realizado com sucesso.")
else:
    print(f"Não foi possível sacar R${valor_saque2:.2f}: saldo insuficiente.")

# Exibindo saldo final
conta1.exibir_saldo()