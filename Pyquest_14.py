print("14. Elabore um programa que leia o salário de um empregado e com base na tabela abaixo calcule e informe sua gratificação e seu salário líquido.")
salario=float(input("Digite o salario: "))

if salario<2000:
    valor=(salario*5)/100
    gratificacao=salario+valor
    print("Gratificação: {} salario liquido: {}".format(valor, gratificacao))
elif salario>2000 and salario<2500:
    valor=(salario*10)/100
    gratificacao=salario+valor
    print("Gratificação: {} salario liquido: {}".format(valor, gratificacao))

elif salario>2500 and salario<=3000:
    valor=(salario*15)/100
    gratificacao=salario+valor
    print("Gratificação: {} salario liquido: {}".format(valor, gratificacao))
else:
    valor=(salario*20)/100
    gratificacao=salario+valor
    print("Gratificação: {} salario liquido: {}".format(valor, gratificacao))