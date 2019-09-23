print("Sejam P(x1,y1) e Q(x2,y2) dois pontos quaisquer do plano. A sua distância é dada por: \nD =(x2 – x1)² + (y2 – y1)²\nElabore um programa que leia as coordenadas dos pontos “P” e “Q”, calcule e escreva sua distância")
x1=int(input("Digite o valor do x1: "))
y1=int(input("Digite o valor do y1: "))
x2=int(input("Digite o valor do x2: "))
y2=int(input("Digite o valor do y2: "))

D=((x2-x1)**2+(y2-y1)**2)**1/2

print(D)