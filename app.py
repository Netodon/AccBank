class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor} realizado. Novo saldo: R${self.saldo}")

    def saque(self, valor):
        if valor > self.saldo:
            print('Saldo Insuficiente.')
        else:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}")
    
    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo}")

def main():
    conta1 = ContaBancaria("Neto")
    conta1.deposito(230)
    conta1.saque(70)
    conta1.consultar_saldo()


if __name__ == "__main__":
    main()