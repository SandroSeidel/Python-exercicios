'''Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista 
e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, 
saldo é opcional, com valor default zero e os demais atributos são obrigatórios.'''

class Account():
    def __init__(self, account_number, client_name, balance = 0):
        self.account_number = account_number
        self.client_name = client_name
        self.balance = balance

    def changeName(self, name):
        self.client_name = name
    
    def set_deposit(self, value):
        self.balance += value 
    
    def get_withdraw(self, ammount):
        if ammount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= ammount
            return ammount

#tests

sandro = Account(324726, 'Sandro Seidel', 1350)

print(f"User: {sandro.client_name} \nAccount number: {sandro.account_number} \nBalance: {sandro.balance}")

sandro.changeName('Sandro Henrique')

sandro.set_deposit(50)

print(f"User: {sandro.client_name} \nAccount number: {sandro.account_number} \nBalance: {sandro.balance}")

sandro.get_withdraw(300)

print(f"User: {sandro.client_name} \nAccount number: {sandro.account_number} \nBalance: {sandro.balance}")

sandro.get_withdraw(2000)
