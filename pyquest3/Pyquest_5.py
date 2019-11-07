print("Construir um programa que leia o salário bruto e o sexo de um funcionário. Se o sexo for “M” (masculino), calcular, armazenar e imprimir um desconto de 5% e o salário líquido, caso contrário, calcular, armazenar e imprimir um desconto de 3% e o salário líquido.")
salario_bruto=float(input("Digite o salario bruto do funcionario: "))
sexo=input("Digite o sexo do funcionario(M OU F): ")
if sexo=='M':
    desconto=(salario_bruto*5)/100
    salario_liquido=salario_bruto-desconto
    print("Salario liquido{}".format(salario_liquido))

else:
    desconto=(salario_bruto*3)/100
    salario_liquido=salario_bruto-desconto
    print("Salario liquido{}".format(salario_liquido))
