"""Faça um programa que leia a idade de 10 pessoas. Ao final escreva a média das idades."""

idade=[]
x=0; total=0


for x in range(0,10):
    idade.append(int(input("Digite a idade: ")))
    total += idade[x]

print(total/10)