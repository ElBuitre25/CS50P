# Making Faces — CS50P Set 0
# Problema: Los programas modernos convierten emoticons de texto a emojis
# automaticamente. Dado un texto ingresado por el usuario, reemplazar
# ":)" por 🙂 y ":(" por 🙁, dejando el resto del texto sin cambios.
# Ejemplo: "Hello :) Goodbye :(" → "Hello 🙂 Goodbye 🙁"

def main():
    word=input("Enter the word: ")
    print(convert(word))


def convert(word):
    new_word=word.replace(":)","🙂").replace(":(","🙁")
    return new_word

main()