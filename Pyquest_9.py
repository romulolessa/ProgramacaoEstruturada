print("O cardápio de uma lanchonete é o seguinte:")
print("Especificação: Código Preço")
print("Cachorro quente: 100 | 5,20")
print("Hambúrguer: 101 | 5,20")
print("Cheeseburguer: 102 | 7,30")
print("Refrigerante: 103 | 5,00")
print("Escrever um algoritmo que leia o código do item pedido, a quantidade e calcule o valor a ser pago por aquele lanche. \nConsidere que a cada execução somente será calculado um item")

codigo=int(input("Digite o codigo do produto"))


if codigo == 100:
    print("Cachorro quente")
    quantidade=int(input("Digite a quantidade:"))
    total=5.2*quantidade
    print("Total a pagar:R$ {}".format(total))
    
elif codigo == 101:
    print("Hambúrguer")
    quantidade=int(input("Digite a quantidade:"))
    total=5.2*quantidade
    print("Total a pagar:R$ {}".format(total))

elif codigo == 102:
    print("Cheeseburguer")
    quantidade=int(input("Digite a quantidade:"))
    total=7.3*quantidade
    print("Total a pagar:R$ {}".format(total))

elif codigo == 103:
    print("Refrigerante")
    quantidade=int(input("Digite a quantidade:"))
    total=5.0*quantidade
    print("Total a pagar:R$ {}".format(total))
else:
    print("Codigo invalido")
    