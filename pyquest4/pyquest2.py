"""
Faça um programa que calcule e escreva no vídeo o somatório dos números inteiros de 1 até 50.
"""
num = 1
cont = 0

for num in range (1,51):
    cont+=num
    num += 1

print(cont)