from operator import truediv




Digito = (1,2,3)
Lista  = (1,2,3)

print("------------------------------------------------------")      


print("Bem-vindo ao sistema municipal de votação!!!")
print("Digite o número respectivo do candidato.")
print("(1) Vitor")
print("(2) Paulo")
print("(3) Mário")     


while True:
    try:
            Digito = int(input("Digite o número do candidato: "))
    except ValueError:
            print(f"Por favor, escolha apenas entre {Lista}.")
            continue
    if Digito == 1:
            confirmação = input("Pressione enter para confirmar o voto.")
            print("Enviado.")
            break
    if Digito == 2:
            confirmação = input("Pressione enter para confirmar o voto.")
            print("Enviado.")
            break
    if Digito == 3:
            confirmação = input("Pressione enter para confirmar o voto.")
            print("Enviado.")
            break
    else:
        print(f"Por favor, escolha apenas entre {Lista}.")



print("------------------------------------------------------")      




