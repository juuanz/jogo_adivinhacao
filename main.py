import random

print("Bem-vindo ao Jogo de Adivinhação")
print("Tente adivinhar o número que eu estou pensando (entre 1 e 100).")

numero_secreto= random.randint(1, 100)
tentativas= 0
acertou= False

while not acertou:
    tentativa= int(input("Digite seu número palpite: "))
    tentativas+= 1

    if tentativa < numero_secreto:
        print("O número secreto é MAIOR")
    elif tentativa > numero_secreto:
        print("O número secreto é MENOR")
    else:
        print(f'Parabéns, você acertou o número secreto {numero_secreto} em {tentativas} tentativas.') 
        acertou= True    
