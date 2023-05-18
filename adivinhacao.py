import random

def jogar():
    print("Bem vindo(a) ao  jogo de Adivinhação!")

    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina um nível: "))


    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5


    for rodada in range (1, total_tentativas + 1):
        print("Tentativa {} de {}". format (rodada, total_tentativas)) 

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Voce digitou", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou  = chute == numero_secreto
        maior  = chute > numero_secreto
        menor  = chute < numero_secreto

        if (acertou):
            print("Parabéns! Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(maior):
                print("Você errou! Chute foi maior.")
                if(rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif(menor):
                print("Você errou! O chute foi menor.")
                if(rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))


    print("Fim do Jogo!")
if(__name__ == "__main__"):
    jogar()

