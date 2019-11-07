print("Certo aço é classificado de acordo com o resultado de três testes, que devem verificar se o mesmo satisfaz às seguintes especificações:")
print("a.Teste 1- conteúdo de carbono abaixo de 7%;")
print("b.Teste 2- dureza Rokwell maior que 50;")
print("c.Teste 3- resistência à tração maior do que 80.000 psi.")

carbono=int(input("Qual a porcentagem de carbono da amostra: "))
rockwell=int(input("Qual a medida em rockwell da amostra: "))
tracao=int(input("Qual a resistencia a tração da amostra: "))


if carbono>7 and rockwell>50 and tracao>80000:
    print("grau 10°")
elif carbono>7 and rockwell>50:
    print("grau 9°")
elif carbono>7:
    print("grau 8°")
else:
    print("grau 7°")