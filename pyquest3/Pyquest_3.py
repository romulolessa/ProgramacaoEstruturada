print("Construir um programa que leia as 2 notas de um aluno e que calcule, armazene e imprima a média. Se a média for maior ou igual a 7, imprimir “Aprovado”, caso contrário, realizar a leitura de uma terceira nota, que terá peso 2 e calcular, armazenar e imprimir uma nova média. Se a nova média for maior ou igual a 6, imprimir “Aprovado”, caso contrário, imprimir “Reprovado”")
nota1=float(input("Digite a primeira nota:"))
nota2=float(input("Digite a segunda  nota:"))

media=(nota1+nota2)/2

if media>=7:
    print("Aprovado")
else:
    nota3=float(input("Digite a terceira nota:"))
    media_final=(nota1+nota2+(nota3*2))/5 #nao entendi como posso fazer essa conta

    if media_final>=6 :
        print("Aprovado{:.2f}".format(media_final))
    else:
        print("Reprovado{:.2f}".format(media_final))