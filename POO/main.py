from optparse import Option
import pprint
import random


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
        self.saldo = random.randrange(1, 10000)

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
                self.saldo += valorDepositado
                print(f"{self.nome} o depósito foi realizado com sucesso")
                return

            elif(valorDepositado < 1):
                print(f"{self.nome} é necessário uma quantia mínima de 1 real para realizar o reposito")
                return
            
        return print(f"Não foi possível realizar o depósito, por favor, abra uma conta e tente novamente")

    def Saque(self, valorSacado):
        if valorSacado < self.saldo:
            print(f"{self.nome} saldo insuficiente para realizar o saque, tente outra quantia")
            return
        
        else:
            self.saldo -= valorSacado
            print(f"{self.nome} saque realizado com sucesso!")

        
    def ExibirSaldo(self):
        if self.AbrirConta():
            print(f"{self.nome} seu saldo é de {self.saldo} reais")
            return
        

        


while Option != 2:
    Option = int(input("""
        Seja Bem Vindo/a ao Banco Central!
        Para realizar as operações disponibilizada, é necessário possuir uma conta.
        
        1 - Criar uma Conta
        2 - Sair
    """))
    if Option == 1:
        print("Para Continuar, é necessário fornecer algumas informações!")
        NomeUserCont = input("Digite o seu nome completo: ")
        IdadeUserCont = int(input("Digite a sua idade: "))
        CpfUserCont = input("Digite a sua idade: ")

        print("Dados pessoais preenchidos! Informe os dados necessários para a abertura da sua conta!")
        Username = input("Digite o Usuário desejado para a Conta: ")
        Email = input("Digite o seu E-mail: ")
        Senha = input("Digite a sua senha: ")
        Conta_User = ContaBanco(NomeUserCont, IdadeUserCont, CpfUserCont, Username, Email, Senha)
        Conta_User.AbrirConta()



# Teste2.ExibirSaldo()
# Teste2.Deposito(100)
# Teste2.ExibirSaldo()