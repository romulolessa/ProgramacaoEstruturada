print("Tendo como dados de entrada a altura e o sexo de uma pessoa (M - masculino e F - feminino), construa um algoritmo que calcule seu peso ideal,\n utilizando as seguintes fórmulas: - para homens: (72.7*h)-58- para mulheres: (62.1*h)-44.7")
h=float(input("Digite sua altura: "))
sexo=input("Digite seu sexo (M - masculino e F - feminino): ")

if sexo=='M':
    peso_ideal=(72.7*h)-58
    print(peso_ideal)
else:
    peso_ideal=(62.1*h)-44.7
    print(peso_ideal)