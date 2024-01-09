import math
from pickle import FALSE, TRUE


class User():
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.contaCriada = False

    
class ContaBanco(User):
    def __init__(self, nome, idade, cpf, nomeUser, email, senha):
        super().__init__(nome, idade, cpf)
        self.nomeUser = nomeUser
        self.email = email
        self.senha = senha
        self.saldo = 0

    def VeridicadorIdade(self):
        if(self.idade < 18):
            print(f"Olá, {self.nome} você não possui idade sufiente para abrir uma conta, é necessário ser maior de 18 anos.")
            return True
        return False

    def AbrirConta(self):
        if self.VeridicadorIdade():
            return False
        print(f"Parabéns, {self.nome}, sua conta foi aberta.")
        return True
    def Deposito(self, valorDepositado):
        if self.AbrirConta():
            if(valorDepositado >= 1):
                self.saldo = valorDepositado
                print(f"{self.nome} o depósito foi realizado com sucesso")
                return

            elif(valorDepositado < 1):
                print(f"{self.nome} é necessário uma quantia mínima de 1 real para realizar o reposito")
                return
            
        return print(f"Não foi possível realizar o depósito, por favor, abra uma conta e tente novamente")

    def ExibirSaldo(self):
        print(f"{self.nome} seu saldo é de {self.saldo} reais")

        



Teste2 = ContaBanco("Luan Matheus Ferreira Costa", 17, "000.000.000-00", "LuanMFC", "luanmatheus198@gmail.com", "123")
Teste2.Deposito(100)
Teste2.ExibirSaldo()