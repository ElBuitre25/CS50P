# Playback Speed — CS50P Set 0
# Problema: Al reproducir audio a velocidad reducida, los espacios entre
# palabras se vuelven notorios. Dado un texto ingresado por el usuario,
# reemplazar cada espacio por tres puntos "..." e imprimir el resultado.
# Ejemplo: "This is CS50" → "This...is...CS50"

print(input("Ingrese el texto: ").replace(" ","..."))