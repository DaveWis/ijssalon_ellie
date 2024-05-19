import math

def discriminant(a,b,c):
    D1 = (-b + math.sqrt(b**2 - 4*a*c))/(2 * a)
    if D1 == 0:
        return "geen oplossing"
    
    D2 = (-b - math.sqrt(b**2 - 4*a*c))/(2 * a)
    if D2 == 0:
        return "geen oplossing"
    
    uitvoer = [D1, D2]
    return uitvoer

print("Voor de formule ax^2 + bx + c, geef a, b en c:")

a = int(input("Wat is a?"))
b = int(input("Wat is b?"))
c = int(input("Wat is c?"))

uitkomst = discriminant(a,b,c)

D1 = uitkomst [0]
D2 = uitkomst [1] 

print(f"Waarde a is {a}. Waarde b is {b}. Waarde c is {c}. Waarde D1 is {D1}. Waarde D2 is {D2}")

