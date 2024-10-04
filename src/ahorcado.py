import random
from os import system

#Falta programación defensiva. NO CONTROLA ERRORES
#Faltan documentar
class Ahorcado:
    def __init__(self):
        self.lista_palabras = ["hola", "manolo", "hoy", "mañana", "pasado"]
        self.letras = list(self.lista_palabras[random.randint(0, len(self.lista_palabras)-1)])
        self.letras_adivinadas = []
        self.vidas = 5
        self.vida_perdida = False

    def tablero(self):
        print("\n")
        print("¡BIENVENIDO AL JUEGO DEL AHORCADO!")
        print("\n")
        if self.vida_perdida:
            print("\tLetra no coincide pierdes una vida")
            print("\n")
            self.vida_perdida = False
        print(f"\tVidas restantes: {self.vidas}")
        print("\n")
        print("\t+---------+")
        print("\t|         |")
        print("\t          |")
        print("\t          |")
        print("\t          |")
        print("\t          |")
        print("\t          |")
        print("\t          |")
        print("\t--------------+")
        for letra in self.letras:
            if letra in (self.letras_adivinadas):
                print(letra, end=" ")
            else:
                print("_", end=" ")
        print("\n")


    def comprobar_letra(self, letra):
        encontradas = 0
        for i in range(len(self.letras)):
            if letra == self.letras[i]:
                self.letras_adivinadas.append(letra)
                encontradas = encontradas + 1
        return encontradas


    def jugar(self):
        system("cls")
        while True:
            self.tablero()
            valor = input("Introduce letra: ")
            if valor == "q":
                system("cls")
                break
            system("cls")
            encontradas = self.comprobar_letra(valor)
            if encontradas > 0:
                print(f"Encontradas: {encontradas}")
            else:
                self.vidas = self.vidas - 1
                self.vida_perdida = True

            if self.vidas == 0:
                print("\n")
                print("TE HAS QUEDADO SIN VIDAS 😭")
                print("\n")
                break

            if len(self.letras_adivinadas) == len(self.letras):
                print("\n")
                print("¡HAS GANADO!")
                print("\n")
                break
        
