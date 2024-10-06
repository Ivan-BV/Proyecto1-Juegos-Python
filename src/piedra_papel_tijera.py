from os import system
import random
from time import sleep

class Piedra_Papel_Tijera:
    def __init__(self):
        self.opciones = ["piedra", "papel", "tijera"]
        self.modalidad = 0 #1 para normal, 2 para lagarto spock
        self.victorias = 0
        self.derrotas = 0
        self.ronda = 0
        self.opcion_jugador = ""
        self.opcion_maquina = ""
        self.reglas = {
            "piedra": ["lagarto", "tijera"],
            "papel": ["piedra", "spock"],
            "tijera": ["papel", "lagarto"],
            "lagarto": ["spock","papel"],
            "spock": ["tijera","piedra"]
            }
        self.titulo_ascii = """    ____  ______________  ____  ___       ____  ___    ____  ________       __________    ____________  ___ 
   / __ \/  _/ ____/ __ \/ __ \/   |     / __ \/   |  / __ \/ ____/ /      /_  __/  _/   / / ____/ __ \/   |
  / /_/ // // __/ / / / / /_/ / /| |    / /_/ / /| | / /_/ / __/ / /        / /  / /__  / / __/ / /_/ / /| |
 / ____// // /___/ /_/ / _, _/ ___ |   / ____/ ___ |/ ____/ /___/ /___     / / _/ // /_/ / /___/ _, _/ ___ |
/_/   /___/_____/_____/_/ |_/_/  |_|  /_/   /_/  |_/_/   /_____/_____/    /_/ /___/\____/_____/_/ |_/_/  |_|
                                                                                                            
"""

    

    def movimiento_maquina(self):
        self.opcion_maquina = self.opciones[random.randint(0, len(self.opciones) - 1)]

    def comprobar_ganador(self):
        print("\n\tTu has elegido: ", self.opcion_jugador)
        print("\n\tLa maquina ha elegido: ", self.opcion_maquina)
        print("\n\tY el ganador es...")
        sleep(2)
        if self.opcion_jugador == self.opcion_maquina:
            print("\n\tHay empate\n")
        elif self.opcion_jugador in self.reglas[self.opcion_maquina]:
            print("\n\tGana la maquina esta ronda\n")
            self.derrotas = self.derrotas + 1
            self.ronda = self.ronda + 1
        else:
            print("\n\tHas ganado esta ronda\n")
            self.victorias = self.victorias + 1
            self.ronda = self.ronda + 1
        self.opcion_jugador = ""
        self.opcion_maquina = ""
        sleep(3)
            
    def tablero(self):
        system("cls")
        print("\n", self.titulo_ascii)
        print("\n\t════════════════════════════════════════════")
        print("\n\t\t", "Ronda", self.ronda + 1, "\n")
        print(f"\t\t  Marcador\n\n\t\tTu {self.victorias} - {self.derrotas} Maquina\n\n")
        print("\t\tOpciones: ")
        print("\n\t\t", end="")
        for opcion in self.opciones:
            print(opcion.capitalize(), end=" ")
        print("\n\n\t════════════════════════════════════════════")

    def iniciar_partida(self):
        system("cls")
        print("\tBienvenido a Piedra, Papel, Tijera")
        print("\n", self.titulo_ascii)
        print("\n\t\t1. Clasico\n\t\t2. Lagarto Spock")
        while self.modalidad == 0:
            modalidad = input("\nIntroduce la modalidad: ")
            if modalidad == "1" or modalidad == "2":
                self.modalidad = modalidad
            else:
                print("Introduce una de las opciones validas")
        if self.modalidad == "2":
            self.opciones.append("lagarto")
            self.opciones.append("spock")
        print("\t\t", "\n\tModalidad clasica elegida" if self.modalidad == "1" else "\n\tModalidad lagarto spock elegida")
        print("\n\t¡Comienza la partida!\n\n\tObjetivo: Gana el mejor de 5 rondas\n\n")

    def jugar(self):
        self.iniciar_partida()
        while True:
            self.tablero()
            eleccion = input("\n\n\t--> ")
            if eleccion.isalpha():
                self.opcion_jugador = eleccion
                self.movimiento_maquina()
                self.comprobar_ganador()
                self.tablero()
            if self.victorias == 3:
                print("\n\t¡Has ganado la partida!")
                sleep(5)
                break
            elif self.derrotas == 3:
                print("\n\tHa ganado la maquina 😢")
                sleep(5)
                break

            