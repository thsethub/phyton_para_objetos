class Pessoa:
    def __init__(self, nome, idade, altura, genero):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.genero = genero

    def falar(self):
            
            print(f"Olá, me chamo {self.nome}, tenho {self.idade} anos, {self.altura} de altura e sou do sexo {self.genero}.")

class estudo(Pessoa):
    def __init__(self,nome, idade, altura, genero, ocupacao, instituicao):

        super().__init__(nome, idade, altura, genero)

        self.ocupacao = ocupacao
        self.instituicao = instituicao

    def atuando(self):
            print(f"{self.nome} é {self.ocupacao}, na {self.instituicao}.")

pessoa = Pessoa("Thiago Augusto","20","1,67","Masculino")
print(pessoa.nome)
pessoa.falar()
estudo = estudo("Thiago Augusto","20","1,67","Masculino","Estudante de Eng. Controle e Automação","UFPE - Universidade Federal de Pernambuco")
print(estudo.instituicao)
print(estudo.ocupacao)
estudo.atuando()
