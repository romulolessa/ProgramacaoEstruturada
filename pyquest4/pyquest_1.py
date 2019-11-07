print("1. Faça um programa que leia o preço de 10 produtos. Ao final escreva o somatório dos preços.")

"""criação de variavel """

produtos=[]
x=0
total=0

"""criação da repetição """
for x in range(0, 10):
    produtos.append(int(input("Digite o preço do produto: ")))
    total += produtos[x]

"""exibição do resultado """

print(total/10)