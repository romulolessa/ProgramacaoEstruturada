print("15. Jogo de Pedra, papel e tesoura: nesse jogo cada jogador faz sua escolha (1 –Tesoura, 2 – Pedra, 3 – Papel), e vence aquele que escolher um objeto que seja capaz de vencer o outro:")
print("Tesoura corta papel")
print("Pedra quebra tesoura")
print("Papel embrulha a pedra")
print("Faça que leia a opção de objeto do primeiro jogador, a opção de objeto do segundo jogador e informe qual jogador venceu (ou se houve empate).")

print("Jogador 1")
jogador1=int(input("Escolha 1-Tesoura, 2- Pedra, 3- Papel: "))

print("Jogador 2")
jogador2=int(input("Escolha 1-Tesoura, 2- Pedra, 3- Papel: "))

if jogador1 ==1:#Tesoura
    if jogador2 ==3:
        print("Tesoura corta papel")
        print("Jogador 1 ganhou!")
    elif jogador2==2:
        print("Pedra quebra tesoura")
        print("Jogador 2 ganhou!")
    else:
        print("Empate!")
elif jogador1 ==2:#pedra
    if jogador2==1:
        print("Pedra quebra tesoura")
        print("Jogador 1 ganhou!")
    elif jogador2==3:
        print("Papel embrulha a pedra")
        print("Jogador 2 ganhou!")
    else:
        print("Empate!")
elif jogador1==3:#Papel
    if jogador2==1:
        print("Tesoura corta papel")
        print("Jogador 2 ganhou!")
    elif jogador2==2:
        print("Papel embrulha a pedra")
        print("Jogador 1 ganhou!")
    else:
        print("Empate!")