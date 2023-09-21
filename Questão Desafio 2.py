nome = []
RG = []
CPF = []
idade = 0

while(len(nome)<2 and idade == 0):
      nome = (input("Digite seu nome e sobrenome: ")).split()
      if(len(nome)<2):
            print("Por favor, digite seu sobrenome também!")

RG = str(input("Digite seu RG, por gentileza: "))
CPF = str(input("Digite seu CPF, por gentileza: "))
idade = int(input("Digite sua idade, por gentileza: "))
print("_______________________________________________________")

print(f"Seja bem vindo!\nUsuário: {nome[0]} {nome[1]}\nRG: {RG}\nCPF: {CPF}\n{idade} anos.")