"""
Faça um programa que leia o preço de 10 produtos. Ao final escreva o somatório dos preços.
"""
produtos=[]
x=0
total=0


for x in range(0, 10):
    produtos.append(int(input("Digite o preço do produto: ")))
    total += produtos[x]

print(total/10)