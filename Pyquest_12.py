print("Fazer um algoritmo para calcular a contribuição ao INSS, IR e a associação de funcionários a partir do salário bruto, que é dado de entrada. \nAs taxas sobre o salário bruto são as seguintes: \nINSS - 10%\nIR - 25%\nSindicato - 0.5 % \nO programa deve imprimir as contribuições e o valor do salário líquido")

salarioBruto=float(input("Digite o salario bruto do funcionario: "))

desconto_inss=(salarioBruto*10)/100
desconto_ir=(salarioBruto*25)/100
desconto_sindicato=(salarioBruto*0.5)/100
salario_liquido=salarioBruto-desconto_inss-desconto_ir-desconto_sindicato

print("INSS: {}\nIR: {}\nassociação de funcionários: {}\nSalario Liquido: {}".format(desconto_inss, desconto_ir, desconto_sindicato, salario_liquido))