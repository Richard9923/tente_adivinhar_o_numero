# Programa originalmente criado com Pycharm64


# jogo adivinhe o número com python


import random



# criar uma funcao para receber um input do usuário referente a dificuldade do jogo

def dificuldadeInput():
    dificuldade = input("Qual o nível de dificuldade que você quer jogar: Facil/Dificil? ").lower()
    if dificuldade == "facil":
        print(f"Você escolheu a dificuldade {dificuldade}.")
        return 10
    else:
        print(f"Você escolheu a dificuldade {dificuldade}.")
        return 5
# funcao para receber o numero random e o input do jogador e fazer a comparacao

def rodandoJogo(tentativaUsuario, numeroRandom):
    if tentativaUsuario == numeroRandom:
        return "certo"
    elif tentativaUsuario > numeroRandom:
        return "acima"
    else:
        return "abaixo"


# criar uma variável onde irei colocar a dificuldade, com o número de tentativas
numeroTentativas = dificuldadeInput()
print(f"Número de tentativas: {numeroTentativas}.")
#numero aleotório
numeroAleotorio = random.randint(0, 100)
# criar uma variavel com um boolean para distinguir se o jogo ainda esta rodando
jogoOn = True
# criar um while loop para manter o jogo rodando, até as tentativas acabarem ou o jogador acertar o número

while jogoOn == True:
    print(f"Restam: {numeroTentativas}. ")
    tentativa = int(input(f"Tente adivinhar o número aleotório de 0 a 100."))
    resultadoJogo = rodandoJogo(tentativa, numeroAleotorio)

    if resultadoJogo == "certo":
        print(f"Você acertou! Número secreto: {numeroAleotorio}.")
        print("O jogo terminou.")
        jogoOn = False
    elif resultadoJogo == "acima":
        numeroTentativas -= 1
        if numeroTentativas == 0:
            print(f"Infelizmente você perdeu o jogo, suas tentativas acabaram.")
            print(f"Número secreto: {numeroAleotorio}.")
            jogoOn = False
        else:
            print("Tentativa acima do número certo.")
            print("Tente novamente.")

    else:
        numeroTentativas -= 1
        if numeroTentativas == 0:
            print(f"Infelizmente você perdeu o jogo, suas tentativas acabaram.")
            print(f"Número secreto: {numeroAleotorio}.")
            jogoOn = False
        else:
            print("Tentativa abaixo do número certo.")
            print("Tente novamente.")



