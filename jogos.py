import adivinhacao
import forca


print("Escolha um jogo!")
print("(1) Adivinhação (2) Forca")

jogo = int(input("Escolha o jogo!"))

if (jogo == 1):
    print("Jogando Adivinhação")
    adivinhacao.jogar()
elif(jogo == 2):
    print("Jogando Forca")
    forca.jogar()
