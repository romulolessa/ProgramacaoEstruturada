"""
Elabore um programa que leia a idade de diversas pessoas e ao
final informe: o total de pessoas cadastradas, a porcentagem
de pessoas com idade inferior a 18 anos, a porcentagem de
pessoas com idade igual ou superior a 18 anos.
"""
pessoa=int(input("Digite a quantidade de pessoas: "))
cont=0; menor=0; maior=0; somamenor=0; somamaior=0
for x in range(pessoa):
    cont += 1
    idade=int(input("Digite a idade: "))
    if idade < 18:
        menor+=1
    elif idade>= 18:
        maior+=1
    else:
        continue
    x+=1
somamenor = (menor * 100)/pessoa
somamaior = (maior *100)/pessoa

print("Total de pessoas: {}".format(pessoa))
print("Porcentagem de pessoas menor de 18 anos:{}% ".format(somamenor))
print("Porcentagem de pessoas maior de 18 anos: {}%".format(somamaior))