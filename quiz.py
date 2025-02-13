# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")

# input
a=int(input("agrege el valor a"))
b=int(input("agrege el valor b"))
c=int(input("agrege el valor c"))


# processing

if a+b>=c:
    r = " se puede formar el triangulo"
elif b+c>=a:
    r = " se puede formar un triangulo"
elif a+c>=b:
    r = " se puede formar un triangulo"
else:
    r = "el triangulo no se puede hacer"

# output
print(r)