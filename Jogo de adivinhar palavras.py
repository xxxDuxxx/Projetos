from secrets import choice
from tracemalloc import stop


nome = input("Digite seu nome: ")


print(f"Olá {nome}!")
print("Bem-vindo ao meu jogo de adivinha palavras!")

print(f"Você deseja ter um tutorial do jogo?")
tutorial = input("Sim/Não: ")
Sim = "Você precisa adivinhar as palavras corretamente e terá apenas 3 vidas! Boa sorte."
Não = "Vamos começar o jogo!"

if tutorial == ("Sim"):
    print(Sim)
    print(Não)
elif tutorial == ("Não"):
    print(Não)

palavra_secreta = "arroz"
chances = 3
digitadas = []

while True:
    if chances <= 0:
        print("Você perdeu!!!")
        break   

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in palavra_secreta:
        print(f"Você acertou a letra {letra}, parabéns!")
    else:
        print(f"Você errou a letra {letra}, tente novamente!")
        digitadas.pop

    secreta_temporária = ""

    for letra_secreta in palavra_secreta:
        if letra_secreta in digitadas:
            secreta_temporária = secreta_temporária + letra_secreta
        else:
            secreta_temporária = secreta_temporária + "*"

    if secreta_temporária == palavra_secreta:
        print("Você conseguiu adivinhar a palavra. Parábens!.")
        print(f"A palavra era {secreta_temporária}.")
        break
    else:
        print(f"A palavra secreta está assim {secreta_temporária}.")
    
    if letra not in palavra_secreta:
        chances = chances - 1

    print(f"Você ainda tem {chances} chances.")
    print()
