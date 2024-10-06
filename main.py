from src.ahorcado import Ahorcado
from src.preguntados import Preguntados
from src.tres_en_raya import Tres_en_raya
from src.piedra_papel_tijera import Piedra_Papel_Tijera
from os import system

#Falta programación defensiva. NO CONTROLA ERRORES
#Falta documentar

def main():
    
    titulo_ascii = """
\t\t     ▒▒▒▒▒▒▒▒▒▄▄▄▄▒▒▒▒▒▒▒
\t\t     ▒▒▒▒▒▒▄▀▀▓▓▓▀█▒▒▒▒▒▒
\t\t     ▒▒▒▒▄▀▓▓▄██████▄▒▒▒▒
\t\t     ▒▒▒▄█▄█▀░░▄░▄░█▀▒▒▒▒
\t\t     ▒▒▄▀░██▄░░▀░▀░▀▄▒▒▒▒
\t\t     ▒▒▀▄░░▀░▄█▄▄░░▄█▄▒▒▒
\t\t     ▒▒▒▒▀█▄▄░░▀▀▀█▀▒▒▒▒▒
\t\t     ▒▒▒▄▀▓▓▓▀██▀▀█▄▀▀▄▒▒
\t\t     ▒▒█▓▓▄▀▀▀▄█▄▓▓▀█░█▒▒
\t\t     ▒▒▀▄█░░░░░█▀▀▄▄▀█▒▒▒
\t\t     ▒▒▒▄▀▀▄▄▄██▄▄█▀▓▓█▒▒
\t\t     ▒▒█▀▓█████████▓▓▓█▒▒
\t\t     ▒▒█▓▓██▀▀▀▒▒▒▀▄▄█▀▒▒
\t\t     ▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      
"""
    opcion_erronea = False
    system("cls")
    while True:
        print("\n\t\t¡BIENVENIDO A LA SALA DE JUEGOS!\n")
        print(f"{titulo_ascii}\n")
        if opcion_erronea == True:
            print("\n\t⚠️ Introduce una opción valida ⚠️\n")
            opcion_erronea == False
        print("\tIntroduce el juego al que quieres jugar:\n")
        print("\t\t 1. Ahorcado 🔮")
        print("\t\t 2. Preguntados 🤓")
        print("\t\t 3. Tres en raya ❌")
        print("\t\t 4. Pierda, papel, tijera 🪨")
        print("\t\t 5. Salir 👋\n")
        opcion = input("\tIntroduce el juego que quieres jugar: ")
        if opcion == "1":
            Ahorcado().jugar()
        elif opcion == "2":
            Preguntados().jugar()
        elif opcion == "3":
            Tres_en_raya().jugar()
        elif opcion == "4":
            Piedra_Papel_Tijera().jugar()
        elif opcion == "5":
            print("\n\n\t\t¡Hasta pronto! 👋\n\n")
            break
        else:
            system("cls")
            opcion_erronea = True
    
if __name__ == "__main__":
    main()