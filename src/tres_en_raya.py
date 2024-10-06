from os import system
import time as t
import random

class Tres_en_raya:
    def __init__(self):
        self.tablero = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.fichas = ['X', 'O']
        self.turno = 0
        self.ficha_jugador = ""
        self.ficha_maquina = ""
        self.ficha_erronea = False
        self.empate = False
        self.victoria = False
        self.derrota = False
        self.terminado = False
        self.titulo_ascii = """  __________  ___________    _______   __   ____  _____  _____ 
 /_  __/ __ \/ ____/ ___/   / ____/ | / /  / __ \/   \ \/ /   |
  / / / /_/ / __/  \__ \   / __/ /  |/ /  / /_/ / /| |\  / /| |
 / / / _, _/ /___ ___/ /  / /___/ /|  /  / _, _/ ___ |/ / ___ |
/_/ /_/ |_/_____//____/  /_____/_/ |_/  /_/ |_/_/  |_/_/_/  |_|
                                                               
"""

    def actualizar_tablero(self):
        system("cls")
        print(f"{self.titulo_ascii}")
        print("\n\n\t═════════════════════════════════════════════════")
        if self.ficha_erronea == True:
            print("\n\t⚠️ Introduce una ficha valida ⚠️")

        if self.ficha_jugador == "":
            ficha = input("\n\tCon que ficha quieres jugar X - O\n\n\t\t--> ")
            if ficha.lower() == "x" or ficha.lower() == "o":
                self.ficha_erronea = False
                self.ficha_jugador = self.fichas[0] if ficha.strip().upper() == self.fichas[0] else self.fichas[1]
                self.ficha_maquina = self.fichas[0] if self.ficha_jugador != self.fichas[0] else self.fichas[1]
                system("cls")
                print(f"{self.titulo_ascii}")
                print("\n\n\t═════════════════════════════════════════════════")
            else:
                self.ficha_erronea = True

        if self.ficha_erronea == False:
            print("\n\t\t", "  Tu turno" if self.turno % 2 == 0 else "Turno maquina")
            print("\n")
            for i in range(len(self.tablero)):
                print("\t\t ", self.tablero[i][0], "|", self.tablero[i][1], "|", self.tablero[i][2])
                if i != 2:
                    print("\t\t", "---|---|---")
            print("\n\n\t═════════════════════════════════════════════════")
        
    
    def reiniciar_tablero(self):
        self.tablero = []
        for i in range(len(self.tablero)):
            list(self.tablero[i]).append([' ', ' ', ' '])

    def comprobar_ganador(self, ficha):
        print(self.tablero)
        for fila in self.tablero:
            if fila[0] == fila [1] == fila[2] != " ":
                self.empate = True
                
        for i in range(len(self.tablero[0])):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] == ficha:
                if ficha == self.ficha_jugador:
                    self.victoria = True
                else:
                    self.derrota = True
            
        for i in range(len(self.tablero[0])):
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] == ficha:
                if ficha == self.ficha_jugador:
                    self.victoria = True
                else:
                    self.derrota = True

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero [2][2] == ficha:
            if ficha == self.ficha_jugador:
                self.victoria = True
            else:
                self.derrota = True
        
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == ficha:
            if ficha == self.ficha_jugador:
                self.victoria = True
            else:
                self.derrota = True

    def movimiento_maquina(self):
        #turno maquina
        if self.terminado == False:
            print("\n\t\t🤔 La maquina esta pensando 🤔")
            t.sleep(random.randint(1, 3))
            while True:
                fila_maquina = random.randint(0, len(self.tablero) - 1)
                columna_maquina = random.randint(0, len(self.tablero) - 1)
                if self.tablero[fila_maquina][columna_maquina] == ' ':
                    self.tablero[fila_maquina][columna_maquina] = self.ficha_maquina
                    break
                self.turno = self.turno + 1

    def movimiento_jugador(self):
        while True:
            print("\n\tElige una fila desde la posición 1 a la 3")
            fila = input("\n\t\t--> ")
            print("\n\tElige una columna desde la posición 1 a la 3")
            columna = input("\n\t\t--> ")
            fila = str(fila)
            columna = str(columna)
            if fila.isdigit() and columna.isdigit():
                fila = int(fila)
                columna = int(columna)
                if fila < 1 or fila > 3:
                    print("\n\t\t⚠️ La fila esta fuera del tablero ⚠️")
                elif columna < 1 or columna > 3:
                    print("\n\t\t⚠️ La columna esta fuera del tablero ⚠️")
                elif self.tablero[fila-1][columna-1] == ' ':
                    self.tablero[fila-1][columna-1] = self.ficha_jugador
                    self.turno = self.turno + 1
                    break
                else:
                    print("\n\t\t⚠️ La celda esta ocupada ⚠️")
            else:
                print("\n\t\t⚠️ Introduce un valor alfanumerico ⚠️")

    def jugar(self):
        system("cls")
        print("\n\t\t¡Bienvenido a Tres en raya!")
        while True:
            self.actualizar_tablero()
            if self.ficha_jugador != "":
                self.movimiento_jugador()
                self.actualizar_tablero()
                self.comprobar_ganador(self.ficha_jugador)
                if self.empate == True:
                    print("\n\tHabeis empatado")
                    self.terminado = True
                if self.victoria == True:
                    print("\n\t¡Has ganado!")
                    self.terminado = True
                if self.derrota == True:
                    print("\n\tLa maquina ha ganado")
                    self.terminado = True
                self.movimiento_maquina()
                self.actualizar_tablero()
                self.comprobar_ganador(self.ficha_maquina)
                if self.empate == True:
                    print("\n\t\tHay empate")
                    self.terminado = True
                if self.victoria == True:
                    print("\n\t\tHas ganado")
                    self.terminado = True
                if self.derrota == True:
                    print("\n\t\tLa maquina ha ganado")
                    self.terminado = True
                if self.terminado == True:
                    respuesta = input("\n\t\t¿Quieres empezar una nueva partida?\n\n\t\t--> ")
                    if respuesta.strip().lower() == "si":
                        self.reiniciar_tablero()
                    else:
                        break
            
            

            
            