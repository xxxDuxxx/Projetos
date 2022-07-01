



from cmath import sqrt


a = int( input("Coeficiente a: ") )
b = int( input("Coeficiente b: ") )
c = int( input("Coeficiente c: ") )

delta = b**2 - (4*a*c)
raizdelta = sqrt(delta)
raiz1 = (-b - raizdelta ) / (2*a)
raiz2 = (-b + raizdelta ) / (2*a)

if delta == 0:
    raiz = -b / (2*a)
    print("Existe uma raíz real.")
    print(f"A raíz real é {raiz}.")
elif delta < 0:
    print("Não existem raízes negativas.")
elif delta > 0:
    print("Existem duas raízes reais.")
    print(f"As raízes são {raiz1} e {raiz2}. ")










