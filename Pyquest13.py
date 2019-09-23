print("Faca um programa que leia tr�s n�meros diferentes e informe o maior deles.\nSe os n�meros digitados nao forem diferentes o programa deve gerar a mensagem: Os valores digitados nao sao diferentes")

n1=int(input("Digite um numero: "))
n2=int(input("Digite um numero: "))
n3=int(input("Digite um numero: "))

if n1>n2 and n1>n3:
    print(n1)
elif n2>n1 and n2>n3:
    print(n2)
elif n3>n1 and n3>n2:
    print(n3)
else:
    print("Os valores digitados nao sao diferentes")