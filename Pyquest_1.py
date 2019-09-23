print("1. Escreva um programa que calcule a quantidade de litros de combustivel gastos em uma viagem, considerando que o automovel consome 1 litro a cada 12 Km. Para obter o consumo, o usuario deve fornecer o tempo gasto na viagem e a velocidade média durante a mesma. Desta forma, será possível obter a distancia percorrida com a seguinte formula DISTÂNCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros com a fórmula LITROS_USADOS = DISTÂNCIA/12. Deve ser fornecido como resposta: a velocidade média, o tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.")

TEMPO= float(input("Quanto tempo durou a viagem: "))
VELOCIDADE= int(input("Qual foi a velocidade media da viagem: "))

DISTANCIA = TEMPO * VELOCIDADE
LITROS_USADOS = DISTANCIA/12

print(" a velocidade média: {}\n o tempo gasto na viagem: {}\n a distância percorrida: {}\n e a quantidade de litros utilizada na viagem: {}".format(VELOCIDADE, TEMPO,  DISTANCIA, LITROS_USADOS))
