from src.ahorcado import Ahorcado
from src.preguntados import Preguntados
from src.tres_en_raya import Tres_en_raya
from src.piedra_papel_tijera import Piedra_Papel_Tijera
from os import system

#Falta programación defensiva. NO CONTROLA ERRORES
#Falta documentar

def main():
    
    dibujo3 = """
\t     ▒▒▒▒▒▒▒▒▒▄▄▄▄▒▒▒▒▒▒▒
\t     ▒▒▒▒▒▒▄▀▀▓▓▓▀█▒▒▒▒▒▒
\t     ▒▒▒▒▄▀▓▓▄██████▄▒▒▒▒
\t     ▒▒▒▄█▄█▀░░▄░▄░█▀▒▒▒▒
\t     ▒▒▄▀░██▄░░▀░▀░▀▄▒▒▒▒
\t     ▒▒▀▄░░▀░▄█▄▄░░▄█▄▒▒▒
\t     ▒▒▒▒▀█▄▄░░▀▀▀█▀▒▒▒▒▒
\t     ▒▒▒▄▀▓▓▓▀██▀▀█▄▀▀▄▒▒
\t     ▒▒█▓▓▄▀▀▀▄█▄▓▓▀█░█▒▒
\t     ▒▒▀▄█░░░░░█▀▀▄▄▀█▒▒▒
\t     ▒▒▒▄▀▀▄▄▄██▄▄█▀▓▓█▒▒
\t     ▒▒█▀▓█████████▓▓▓█▒▒
\t     ▒▒█▓▓██▀▀▀▒▒▒▀▄▄█▀▒▒
\t     ▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      
"""
    
    system("cls")
    while True:
        print("\n\t¡BIENVENIDO A LA SALA DE JUEGOS!\n")
        print(f"{dibujo3}\n")
        print("\tINTRODUCE EL NUMERO DE LA OPCION QUE QUIERES JUGAR:\n")
        print("\t\t 1. Ahorcado 🔮")
        print("\t\t 2. Preguntados 🤓")
        print("\t\t 3. Tres en raya ❌")
        print("\t\t 4. Pierda, papel, tijera 🪨")
        print("\t\t 6. Salir 👋\n")
        opcion = input("\tIntroduce el juego que quieres jugar: ")
        if opcion == "1":
            Ahorcado().jugar()
        if opcion == "2":
            Preguntados().jugar()
        if opcion == "3":
            Tres_en_raya().jugar()
        if opcion == "4":
            Piedra_Papel_Tijera().jugar()
        if opcion == "6":
            print("\n")
            print("Hasta luego 👋")
            print("\n")
            break
    
if __name__ == "__main__":
    main()