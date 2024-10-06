import time as t
import random

class Tres_en_raya:
    def __init__(self):
        self.tablero = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.fichas = ['X', 'O']
        self.turno = 0
        self.ficha_jugador = ""
        self.ficha_maquina = ""
        self.terminado = False

    def inicializar_tablero(self):
        if self.ficha_jugador == "":
            ficha = input("\tCon que ficha quieres jugar X - O: ")
            self.ficha_jugador = self.fichas[0] if ficha.strip().upper() == self.fichas[0] else self.fichas[1]
            self.ficha_maquina = self.fichas[0] if self.ficha_jugador != self.fichas[0] else self.fichas[1]
        print("\t\t", "Tu turno" if self.turno % 2 == 0 else "Turno de la maquina")
        print("\n")
        for i in range(len(self.tablero)):
            print("\t\t ", self.tablero[i][0], "|", self.tablero[i][1], "|", self.tablero[i][2])
            if i != 2:
                print("\t\t", "---|---|---")
        print("\n")
    
    def reiniciar_tablero(self):
        pass

    def comprobar_ganador(self):
        for fila in self.tablero:
            if fila[0] == fila [1] == fila[2] != " ":
                self.terminado = True
        
    def movimiento_maquina(self):
        #turno maquina
        
        t.sleep(0.5)
        print("\t\tla maquina esta pensando...")
        t.sleep(random.randint(2, 5))
        while True:
            fila_maquina = random.randint(0, len(self.tablero) - 1)
            columna_maquina = random.randint(0, len(self.tablero) - 1)
            if self.tablero[fila_maquina][columna_maquina] == ' ':
                self.tablero[fila_maquina][columna_maquina] = self.ficha_maquina
                break
        self.turno = self.turno + 1

    def movimiento_jugador(self, fila, columna):
        self.tablero[int(fila)][int(columna)] = self.ficha_jugador
        self.turno = self.turno + 1

    def jugar(self):
        while True:
            self.inicializar_tablero()
            fila = input("\tElige fila: ")
            columna = input("\tElige columna: ")
            if (fila or columna) == "q":
                break
            self.movimiento_jugador(fila, columna)
            self.inicializar_tablero()
            self.comprobar_ganador()
            self.movimiento_maquina()
            self.inicializar_tablero()
            self.comprobar_ganador()
            if self.terminado == True:
                print("Todo el tablero ha sido rellenado")
                respuesta = input("Quieres empezar una nueva partida: ")
                if respuesta.strip().lower() == "si":
                    self.reiniciar_tablero()
                else:
                    break
            

            
            