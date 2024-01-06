class Empresa():
    def __init__(self, Nome_Empresa, Anos_Funcionamento, Funcionarios,Contratando):
        self.Nome_Empresa = Nome_Empresa
        self.Anos_Funcionamento = Anos_Funcionamento
        self.Funcionarios = [{Funcionarios}]
        self.Contratando = Contratando

    def Contratar_Funcionario(self):
        pass

    def Demitir_Funcionario(self):
        pass

    def Exibir_Funcionario(self):
        return print(self.Funcionarios)

class Colaborador(Empresa):
    def __init__(self, Nome, Idade, CPF, Cargo, Salario):
        self.Nome = Nome
        self.Idade = Idade
        self.CPF = CPF
        self.Cargo = Cargo
        self.Salario = Salario
        print("aaaaaaaaaaaa", self.Nome)
    
class RH(Empresa):
    index = 0
    cont = index 
    def __init__(self, Contratando, Nome_Colaborador, Idade_Colaborador, CPF_Colaborador, Cargo_Colaborador, Salario_Colaborador):
        self.Contratando = Contratando
        self.Nome_Colaborador = Nome_Colaborador 
        if(self.Contratando == True):
            self.Idade_Colaborador = Idade_Colaborador
            self.CPF_Colaborador = CPF_Colaborador
            self.Cargo_Colaborador = Cargo_Colaborador
            self.Salario_Colaborador = Salario_Colaborador

        elif(self.Contratando == False):
            print(f"Desculpe ", self.Nome_Colaborador, f" não estamos contratando no momento")

    def Contratar_Funcionario(self):
        if(self.Contratando == False):
            return print("Não estamos CONTRATANDO no momento, obrigado!")

        elif(self.Contratando == True):
            novo_funcionario = Colaborador(self.Nome_Colaborador, self.Idade_Colaborador, self.CPF_Colaborador, self.Cargo_Colaborador, self.Salario_Colaborador)
            Empresa("Coca-Cola", 19, novo_funcionario, self.Contratando)
            print(novo_funcionario)
            return print("Funcionário Contratado")

RHTeste = RH(False, "Luan Matheus Ferreira Costa", 19, "000.000.000-00", "Auxiliar de TI", 1200)
RHTeste.Contratar_Funcionario()