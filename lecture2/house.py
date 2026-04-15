def main():
    room = input("wich room will you enter ")
    time = int(input("At what time will you enter?"))
    house_action(room,time)


def house_action(room,time=0):
    match room:
        case "kitchen":
            print("Encender extractor y luz cálida")
        case "hall":
            print("Encender TV y ajustar luz ambiental")
        case "bedroom":
            print("Bajar persianas y activar modo silencio")
            if time>22:
                print("Activando modo nocturno completo")
        case "garage" if time>22:
            print("Activar puertas blindadas")
            
        case "garage":
            print("Abrir puerta y encender luz de seguridad")
        
        case _:
            print("That room is unknown")


main()