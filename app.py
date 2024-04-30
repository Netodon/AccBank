class ContaBancaria:
    def __init__(self, titular, saldo=0, limite_saldo=5000, limite_saques=3):
        self.titular = titular
        self.saldo = saldo
        self.limite_saldo = limite_saldo
        self.limite_saques = limite_saques
        self.saques_realizados = 0
        self.historico_transacoes = []

    def deposito(self, valor):
        self.saldo += valor
        self.historico_transacoes.append(f"Depósito de R${valor} realizado.")
        print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")

    def saque(self, valor):
        if self.saldo - valor < 0:
            print('Saldo Insuficiente.')
        elif self.saques_realizados >= self.limite_saques:
            print('Limite de saques atingido para este mês.')
        else:
            self.saldo -= valor
            self.saques_realizados += 1
            self.historico_transacoes.append(f"Saque de R${valor} realizado.")
            print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo}")

    def consultar_historico_transacoes(self):
        print("Histórico de Transações:")
        for transacao in self.historico_transacoes:
            print(transacao)

def main():
    conta1 = ContaBancaria("Neto")
    conta1.deposito(230)
    conta1.saque(70)
    conta1.saque(50)
    conta1.saque(20)  # Isso excederá o limite de saques
    conta1.consultar_saldo()
    conta1.consultar_historico_transacoes()


if __name__ == "__main__":
    main()