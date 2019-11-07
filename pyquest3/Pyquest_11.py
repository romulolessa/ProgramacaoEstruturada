print("Um banco concederá um crédito especial aos seus clientes, variável com o saldo médio no último ano. \nFaça um algoritmo que leia o saldo médio de um cliente e calcule o valor do crédito de acordo com a tabela abaixo. \nMostre uma mensagem informando o saldo médio e o valor do crédito.")
salario_anual=int(input("Digite a media do saldo medio anual do cliente: "))

if salario_anual<=200:
    print("Saldo medio do ano passado:{} \ncredito: credito nao disponivel".format(salario_anual))
elif salario_anual>=201 and salario_anual<=400:
    credito=(salario_anual*20)/100
    print("Saldo medio do ano passado:{} \ncredito disponivel:{}".format(salario_anual, credito))
elif salario_anual>=401 and salario_anual<=600:
    credito=(salario_anual*30)/100
    print("Saldo medio do ano passado:{} \ncredito disponivel:{}".format(salario_anual, credito))
else:
    credito=(salario_anual*40)/100
    print("Saldo medio do ano passado:{} \ncredito disponivel:{}".format(salario_anual, credito))
    