import random
from os import system
import string
import re

class Ahorcado:
    def __init__(self):
        self.lista_palabras_2 = [
    "zanahoria", "pistola", "elefante", "ketchup", "almohada", "dinosaurio", 
    "gorra", "queso", "viento", "fresa", "internet", "juguete", "libro", 
    "bosque", "mariposa", "cielo", "robot", "tesoro", "orquesta", "yogur", 
    "hormiga", "diamante", "serpiente", "espada", "zorro", "teclado", "manzana", 
    "piscina", "nube", "jardín", "puente", "camión", "lámpara", "vela", 
    "zapato", "silla", "helado", "pájaro", "guitarra", "arena", "tren", 
    "lago", "murciélago", "nariz", "cinturón", "taburete", "hoja", "bajo", 
    "caballo", "volcán", "teléfono", "koala", "oso", "estrella", "alce", 
    "burbuja", "camisa", "isla", "ventana", "reloj", "pastel", "gato", 
    "pingüino", "quesadilla", "dragón", "árbol", "sombra", "uva", "sopa", 
    "piedra", "tigre", "sol", "batería", "ratón", "arcoiris", "pluma", 
    "bufanda", "flor", "cerdo", "palmera", "león", "flauta", "globo", 
    "zapato", "moneda", "bala", "foca", "yate", "almendra", "dado", "mazorca", 
    "muralla", "quimera", "trineo", "hacha", "paraguas", "grillo", "huevo", 
    "calabaza", "sal", "pantalla", "nave", "tijeras", "raqueta", "moto", 
    "yate", "radio", "mar"
    ]
        self.dibujos = [
    """ 
\t\t  +---+
\t\t  |    
\t\t  |    
\t\t  |    
\t\t  |    
\t\t  |    
\t\t======= """,
    """ 
\t\t  +---+
\t\t  |   O
\t\t  |    
\t\t  |    
\t\t  |    
\t\t  |    
\t\t======= """,
    """ 
\t\t  +---+
\t\t  |   O
\t\t  |   |
\t\t  |    
\t\t  |    
\t\t  |    
\t\t======= """,
    """ 
\t\t  +---+
\t\t  |   O
\t\t  |  /|
\t\t  |    
\t\t  |    
\t\t  |    
\t\t======= """,
    """ 
\t\t  +---+
\t\t  |   O
\t\t  |  /|\\
\t\t  |    
\t\t  |    
\t\t  |    
\t\t======= """,
    """ 
\t\t  +---+
\t\t  |   O
\t\t  |  /|\\
\t\t  |  / 
\t\t  |    
\t\t  |    
\t\t======= """,
    """ 
\t\t  +---+
\t\t  |   O
\t\t  |  /|\\
\t\t  |  / \\
\t\t  |    
\t\t  |    
\t\t======= """
]

        self.lista_palabras = ["hola", "manolo", "hoy", "mañana", "pasado"]
        self.letras = list(self.lista_palabras[random.randint(0, len(self.lista_palabras)-1)])
        self.letras_adivinadas = []
        self.vidas = len(self.dibujos)
        self.fallos = 0
        self.vida_perdida = False


    def tablero(self):
        print("\n¡BIENVENIDO AL JUEGO DEL AHORCADO!\n")
        #Esto lo utilizo para mostrar mensaje personalizado y colocado debajo del titulo
        if self.vida_perdida:
            print("\tLetra no coincide pierdes una vida")
            print("\n")
            self.vida_perdida = False
        #Monto el dibujo
        print(f"\tVidas restantes: {self.vidas}")
        print("\n")
        print(f"{self.dibujos[self.fallos]}\n")
        #Preparo las lineas que representan la palabra y si hay alguna acertada la muestro
        print("\t\t", end=" ")
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
            try:
                self.tablero()
                valor = input("Introduce letra: ")
                #Hago limpieza de valor

                if valor.isalpha() and valor != r"!\"#\$%&'\(\)\*\+,-\.\/:;<=>\?@\[\\\]\^_`\{\|\}~" and len(valor) == 1:
                    valor = valor.strip().lower()
                    if valor == "q":
                        system("cls")
                        break
                    system("cls")
                    encontradas = self.comprobar_letra(valor)
                    if encontradas > 0:
                        print(f"Encontradas: {encontradas}")
                    else:
                        self.vidas = self.vidas - 1
                        self.fallos = self.fallos + 1
                        self.vida_perdida = True

                    if self.vidas == 0:
                        print("\n")
                        print(f"{self.dibujos[self.fallos-1]}\n")
                        print("\t  TE HAS QUEDADO SIN VIDAS 😭")
                        print("\n")
                        break

                    if len(self.letras_adivinadas) == len(self.letras):
                        print("\n")
                        print("\t  🎉🎉🎉 ¡HAS GANADO! 🎉🎉🎉")
                        print("\n")
                        break
                else:
                    system("cls")
                    if len(valor) > 1:
                        print("Introduce letra a letra. No introduzca 2 o más letras a la vez")
                    elif len(valor) == 0:
                        print("Introduce al menos una letra")
                    else:
                        print("Introduce una letra entre la A y la Z")
            except ValueError:
                print("Valor erroneo")
            except TypeError:
                print("Tipo erroneo")
        
