print("Faça um programa que leia a idade de 10 pessoas. Ao final escreva a média das idades.")

"""criação de variavel """
idade=[]
x=0; total=0

"""criação da repetição """
for x in range(0,10):
    idade.append(int(input("Digite a idade: ")))
    total += idade[x]

"""exibição do resultado """
print(total/10)