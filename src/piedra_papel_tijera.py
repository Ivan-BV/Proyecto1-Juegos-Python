from os import system


class Piedra_Papel_Tijera:
    def __init__(self):
        self.opciones = ["piedra", "papel", "tijera"]
        self.modalidad = 0 #1 para normal, 2 para lagarto spock
        self.turno = 0
        self.opcion_jugador = ""
        self.opcion_maquina = ""

    def reiniciar_partida(self):
        pass

    def movimiento_maquina(self):
        pass

    def comprobar_ganador(self):
        pass

    def iniciar_partida(self):
        system("cls")
        print("Bienvenido a Piedra, Papel, Tijera")
        print("\n\t\t1. Clasico\n\t\t2. Lagarto Spock")
        modalidad = input("Introduce la modalidad: ")
        if int(modalidad) == 2:
            self.opciones.append("lagarto")
            self.opciones.append("spock")
        print("\t\t", "Modalidad clasica elegida" if modalidad == 1 else "Modalidad lagarto spock elegida")
        print(self.opciones)

    def jugar(self):
        self.iniciar_partida()
        while True:
            break