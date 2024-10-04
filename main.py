from src.ahorcado import Ahorcado
from src.preguntados import Preguntados
from os import system

#Falta programación defensiva. NO CONTROLA ERRORES
#Falta documentars

def main():
    while True:
        print("BIENVENIDO A LA SALA DE JUEGOS")
        print("INTRODUCE EL NUMERO DE LA OPCION QUE QUIERES JUGAR:")
        print("\t1. Ahorcado")
        print("\t2. Preguntados")
        print("\t3. Tres en raya")
        print("\t4. Pierda, papel, tijera")
        print("\t6. Salir")
        opcion = input("Introduce el juego que quieres jugar:")
        if opcion == "1":
            Ahorcado().jugar()
        if opcion == "2":
            Preguntados().jugar()
        if opcion == "6":
            print("\n")
            print("Hasta luego 👋")
            print("\n")
            break
    
if __name__ == "__main__":
    main()