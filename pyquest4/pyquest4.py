"""
Elabore um programa que leia o sexo de um número indeterminado de pessoas.
Ao final escreva a quantidade de pessoas cadastradas e o total de pessoas de cada sexo.
"""
sexo=[]
cont=0

while cont <= 10:
    print("Digite M para masculino e F para feminino")
    s=(input("Digite o sexo: ").upper()
    if s in "MF" :
        sexo.append(s)
        cont += 1
    else:
        print("Letra invalida!")
        break
print(sexo)