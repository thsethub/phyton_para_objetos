lista = [1,2,3,4,5,6,7,8,9,10]
nome = ["Ana","Jackson","Hannah","TeneT","Joe"]
nome_invertido_minusculo = []
nome_minusculo = []
nome2 = []
idade = 0
valor_par = 0
valor_total = 0
i = 0
v = 0
print("1° Questão")
print("___________________________________________")
for pares in lista:
        if (pares % 2 == 0):
                valor_par+=pares
print(valor_par)
print("2° Questão")
print("___________________________________________")
for lista2 in lista:
        valor_total+=lista2
        i+=1

media = valor_total/i
print(media)
print("3° Questão")
print("___________________________________________")
for string in nome:
    nome_minusculo_invertido = string.lower()
    nome_invert = nome_minusculo_invertido[::-1]  # Inverte a string
    nome_invertido_minusculo.append(nome_invert)

for string in nome:
    nome_generico = string.lower()
    nome_minusculo.append(nome_generico)

while(v<=4):
      if(nome_minusculo[v]==nome_invertido_minusculo[v]):
            print(f'Este nome {nome_minusculo[v]} é um palíndromo!')
            v+=1
      else:
            print(f'Este nome {nome_minusculo[v]} não é um palíndromo!')
            v+=1


print("4° Questão e 5° Questão")
print("___________________________________________")
while(len(nome2)<2):
      nome2 = (input("Digite seu nome e sobrenome: ")).split()
      if(len(nome2)<2):
            print("Por favor, digite seu sobrenome também!")
      else:
            print(f"Seja bem vindo {nome2[0]} {nome2[1]}!")
while(idade==0):
    if(idade==0):
      idade=int(input("Digite sua idade válida, por gentileza: "))
print(f"{nome2[0]} {nome2[1]}, sua idade é {idade}!")




