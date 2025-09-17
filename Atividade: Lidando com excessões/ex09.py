#Crie uma função sacar(saldo, valor) que:

#Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo.
#Caso contrário, retorne o novo saldo. Teste a função dentro de um try-except e exiba uma mensagem apropriada ao usuário

class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")
    return saldo - valor

try:
    saldo_atual = 100
    valor_saque = float(input("Digite o valor para sacar: "))
    novo_saldo = sacar(saldo_atual, valor_saque)
    print(f"Saque realizado com sucesso! Novo saldo: R${novo_saldo:.2f}")
except SaldoInsuficienteError as e:
    print("Erro:", e)
except ValueError:
    print("Erro: valor inválido. Digite um número válido.")
