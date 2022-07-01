while True:
    try:
        n1 = int(input(" Digite um número: "))
        n2 = int(input(" Digite outro número: "))
    except ValueError:
        print("Digite apenas números.")
        continue
    
    
    operações = input("""
    
 Digite um sinal de operação aritmética: 

 + para adição.
 - para subtração.
 x para multiplicação.
 / para divisão.
    
 """)
    
 
    if operações == "+" :
            print(f"{n1} + {n2} = {n1 + n2}")
            

    if operações == "-" :
            print(f"{n1} - {n2} = {n1 - n2}")
            

    if operações == "x" :
            print(f"{n1} ** {n2} = {n1 ** n2}")
            

    if operações == "/" :
            print(f"{n1} / {n2} = {n1 / n2}")
    
            