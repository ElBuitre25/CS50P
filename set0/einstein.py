# Einstein — CS50P Set 0
# Problema: Usando la formula de equivalencia masa-energia de Einstein (E = mc²),
# dado un valor de masa en kilogramos ingresado por el usuario, calcular e imprimir
# la energia equivalente en Joules. La velocidad de la luz es 300,000,000 m/s.
# Ejemplo: m=1 → 90000000000000000

def main():
    mass=int(input("m:"))
    print(energy(mass))


#Calcula la energia dada una masa
def energy(mass):
    ligh_speed_square=300000000**2
    return mass*ligh_speed_square



main()