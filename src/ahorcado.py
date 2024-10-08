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

        #self.lista_palabras = ["hola", "manolo", "hoy", "mañana", "pasado"]
        self.letras = list(self.lista_palabras_2[random.randint(0, len(self.lista_palabras_2)-1)])
        self.letras_adivinadas = []
        self.vidas = len(self.dibujos)
        self.letra = ''
        self.fallos = 0
        self.vida_perdida = False
        self.encontradas = 0
        self.input_erroneo = False
        self.titulo_ascii = """    ___    __  ______  ____  _________    ____  ____ 
   /   |  / / / / __ \/ __ \/ ____/   |  / __ \/ __ \\
  / /| | / /_/ / / / / /_/ / /   / /| | / / / / / / /
 / ___ |/ __  / /_/ / _, _/ /___/ ___ |/ /_/ / /_/ / 
/_/  |_/_/ /_/\____/_/ |_|\____/_/  |_/_____/\____/  
                                                     """


    def tablero(self):
        print(f"\n{self.titulo_ascii}\n")
        print("\t╔════════════════════════")
        if self.input_erroneo == True:
            if len(self.letra) > 1:
                print("\n\t⚠️ Introduce una letra a la vez ⚠️")
            elif len(self.letra) == 0:
                print("\n\t⚠️ Introduce al menos una letra ⚠️")
            else:
                print("\n\t⚠️ Introduce una letra entre la A y la Z ⚠️")
        else:
            if self.vida_perdida:
                print("\n\tLa letra no coincide pierdes una vida")
                print()
                self.vida_perdida = False
            if self.encontradas > 0:
                print(f"\n\t    Encontradas: {self.encontradas}")
        #Monto el dibujo
        print(f"\n\t    Vidas restantes: {self.vidas}")
        print(f"\n{self.dibujos[self.fallos]}\n")
        #Preparo las lineas que representan la palabra y si hay alguna acertada la muestro
        print("\n\t", "     ", end=" ")
        for letra in self.letras:
            if letra in self.letras_adivinadas:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        print("\n\n\t════════════════════════╝")


    def comprobar_letra(self):
        """Metodo para comprobar la letra introducida

        Returns:
            bool: determina si la partida a finalizado
        """
        if self.letra.isalpha() and self.letra != r"!\"#\$%&'\(\)\*\+,-\.\/:;<=>\?@\[\\\]\^_`\{\|\}~" and len(self.letra) == 1:
            self.input_erroneo = False
            self.letra = self.letra.strip().lower()
            system("cls")

            self.encontradas = 0
            for i in range(len(self.letras)):
                if self.letra == self.letras[i]:
                    self.letras_adivinadas.append(self.letra)
                    self.encontradas = self.encontradas + 1

            if self.encontradas == 0:
                self.vidas = self.vidas - 1
                self.fallos = self.fallos + 1
                self.vida_perdida = True
            
            if self.vidas == 0:
                print("\n")
                print(f"{self.dibujos[self.fallos-1]}\n")
                print("\t  TE HAS QUEDADO SIN VIDAS 😭")
                print("\n")
                return False

            if len(self.letras_adivinadas) == len(self.letras):
                print("\n")
                print("\t  🎉🎉🎉 ¡HAS GANADO! 🎉🎉🎉")
                print("\n")
                return False
        else:
            self.input_erroneo = True

    def jugar(self):
        system("cls")
        print("\n\t¡BIENVENIDO AL JUEGO DEL AHORCADO!\n")
        while True:
            try:
                self.tablero()
                self.letra = input("\n\tIntroduce letra: ")
                if self.comprobar_letra() == False:
                    break
                system("cls")
            except ValueError:
                print("Valor erroneo")
            except TypeError:
                print("Tipo erroneo")
        
