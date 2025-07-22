import random


numero_sorteado = random.randint (1,50)

acertou = False
while acertou == False:

    numero_escolhido = int(input('Qual número você escolhe?'))
    if numero_escolhido > numero_sorteado:
        print ('Chutou alto!')
    elif numero_escolhido < numero_sorteado:
        print ('Chutou baixo!')

    elif numero_escolhido == numero_sorteado:
        acertou = True
        print ('Você ganhou!')
