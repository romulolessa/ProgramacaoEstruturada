﻿print("Escreva um programam que calcule o índice de massa corpórea (IMC) de uma pessoa, sendo o peso e a altura fornecidos pelo teclado.\nApresentar na tela o peso, a altura e o IMC calculado.Exemplo: \nValores fornecidos pelo teclado: Peso = 60kg e Altura = 1,67m Cálculo do IMC = 60 / (1,67)² = 60 / 2,78 = 21,5")
peso=float(input("DIgite seu peso: "))
altura=float(input("Digite sua altura: "))
imc=peso/altura**2
print("seu imc: {:.1f}".format(imc))