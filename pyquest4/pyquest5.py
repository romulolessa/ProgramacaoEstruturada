"""
Crie um programa que leia a altura de um número indeterminado
de pessoas. Ao final o programa deve informar o total de
pessoas cadastradas, a quantidade de pessoas com altura
inferior a 1,60 metros; a quantidade de pessoas com altura
entre 1,60 metros e 1,80 metros e a quantidade de pessoas com
altura superior a 1,80 metros.
"""
x=int(input("Digite a quantidade de pessoas: "))
cont=0; cont2=0; cont3=0

for x in range(5):
    altura=float(input("Digite a altura: "))
    if altura < 1.60 :
        cont+=1
    elif altura <=1.60 and altura <=1.80:
        cont2+=1
    elif altura >1.80:
        cont3+=1
    else:
        break
print("Quantidade de pessoas com menos de 1.60: {}".format(cont))
print("Quantidade de pessoas entre 1.60 e 1.80: {}".format(cont2))
print("Quantidade de pessoas maior de 1.80:  {}".format(cont3))