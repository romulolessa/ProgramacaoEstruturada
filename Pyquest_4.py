print("Construir um programa leia um número inteiro entre 1 e 7 e imprima o nome do dia da semana correspondente ao número, caso o número esteja fora do intervalo entre 1 e 7, imprimir “DiaInválido”")
dia=int(input("Digite um numero de 1 a 7: "))
if dia==1:
    print("Domingo")
elif dia==2:
    print("Segunda-feira")
elif dia==3:
    print("Terça-feira")
elif dia==4:
    print("Quarta-feira")
elif dia==5:
    print("Quinta-feira")
elif dia==6:
    print("Sexta-feira")
elif dia==7:
    print("Sabado")
else:
    print("Dia Inválido")