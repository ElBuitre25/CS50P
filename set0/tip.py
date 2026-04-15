# Tip Calculator — CS50P Set 0
# Problema: Calcular la propina de una comida en restaurante. El usuario ingresa
# el costo de la comida en formato "$##.##" y el porcentaje de propina en formato
# "##%". El programa calcula e imprime la propina a dejar en formato "Leave $X.XX".
# Ejemplo: $50.00 + 15% → Leave $7.50

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    my_float=float(dollars.removeprefix('$'))
    return my_float


def percent_to_float(percent):
    formated_percent=float(percent.removesuffix('%'))/100
    return formated_percent


main()