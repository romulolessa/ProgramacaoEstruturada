print("Elabore um programa que leia o sexo de um número indeterminado de pessoas. Ao final escreva a quantidade de pessoas cadastradas e o total de pessoas de cada sexo.")

sexo=[]
cont=0

while cont <=10:
    print("Digite M para masculino e F para feminino")
    sexo.append(input("Digite o sexo: "))
    if sexo == 'M' or 'F' or 'f' or 'm':
        cont+=1
    else:
        break 

print(sexo)