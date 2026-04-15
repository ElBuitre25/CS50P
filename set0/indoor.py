# Indoor Voice — CS50P Set 0
# Problema: Escribir en mayusculas es como gritar. Dado un texto ingresado
# por el usuario (en cualquier combinacion de mayusculas/minusculas),
# imprimir ese mismo texto completamente en minusculas.
# La puntuacion y los espacios deben mantenerse sin cambios.
# Ejemplo: "HELLO" → "hello" | "THIS IS CS50" → "this is cs50"

def main():
    palabra=solicitud()
    print(minuscula(palabra))





#Se encarga de solicitar los datos al usuario y devuelve el dato obtenido
def solicitud():
    palabra=input("Ingrese el texto: ")

    return palabra 

#Se encarga de convertir la palabra a minusculas
def minuscula(mayuscula):
    
    palabra_minus=mayuscula.lower()

    return palabra_minus



main()