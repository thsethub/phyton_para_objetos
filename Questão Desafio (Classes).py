class Pessoas:
    def __init__(self, nome, idade, altura, genero):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.genero = genero

    def falar(self):
            
            print(f"Olá, me chamo {self.nome}, tenho {self.idade} anos, {self.altura} de altura e sou do sexo {self.genero}.")

class estudo(Pessoas):
    def __init__(self,nome, idade, altura, genero, ocupacao, instituicao):

        super().__init__(nome, idade, altura, genero)

        self.ocupacao = ocupacao
        self.instituicao = instituicao

    def atuando(self):
            print(f"{self.nome} é {self.ocupacao}, na {self.instituicao}.")



class Pessoa:
    def _init_(self, nome, idade, cpf, rg, endereco, plano, qtd_automacoes):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.rg = rg
        self.endereco = endereco
        self.plano = plano
        self.qtd_automacoes = qtd_automacoes

    def _str_(self):
        return(f"Nome: {self.nome}\nIdade: {self.idade}\nCPF: {self.cpf}\nRG: {self.rg}\nEndereço: {self.endereco}\nPlano: {self.plano}\nQuantidade de Automações: {self.qtd_automacoes}")
        

    def cadastrar():
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        cpf = input("Digite o CPF: ")
        rg = input("Digite o RG: ")
        endereco = input("Digite o endereço: ")
        plano = input("Digite o plano: ")
        qtd_automacoes = input("Digite a quantidade de automações: ")
        
        return Pessoa(nome, idade, cpf, rg, endereco, plano, qtd_automacoes)


op = int(input("Escreva qual opção: 1, 2, 3, 4\nResposta: "))

if (op == 1):
   pessoa = Pessoa.cadastrar()
   print("\nInformações da pessoa:")
   print(pessoa)
    
#pessoa = Pessoa("Thiago Augusto","20","1,67","Masculino")
#print(pessoa.nome)
#pessoa.falar()
#estudo = estudo("Thiago Augusto","20","1,67","Masculino","Estudante de Eng. Controle e Automação","UFPE - Universidade Federal de Pernambuco")
#print(estudo.instituicao)
#print(estudo.ocupacao)
#estudo.atuando()
#print('_____________________________________________')
