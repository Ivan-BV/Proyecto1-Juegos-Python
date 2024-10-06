import random
from os import system

#Falta comprobar si funciona bien que no se repita ninguna pregunta
#Falta control de errores

class Preguntados:
    def __init__(self):
        self.diccionario_preguntas_2 = {
    "Ciencia": {
        1: {
            "pregunta": "¿Cuál es el planeta más cercano al Sol?",
            "opciones": ["a) Venus", "b) Marte", "c) Mercurio", "d) Júpiter"],
            "respuesta_correcta": "c"
        },
        2: {
            "pregunta": "¿Qué científico propuso la teoría de la relatividad?",
            "opciones": ["a) Isaac Newton", "b) Galileo Galilei", "c) Albert Einstein", "d) Nikola Tesla"],
            "respuesta_correcta": "c"
        },
        3: {
            "pregunta": "¿Qué gas es necesario para la respiración de los seres humanos?",
            "opciones": ["a) Hidrógeno", "b) Nitrógeno", "c) Oxígeno", "d) Helio"],
            "respuesta_correcta": "c"
        },
        4: {
            "pregunta": "¿Cuál es el metal más ligero?",
            "opciones": ["a) Oro", "b) Hierro", "c) Litio", "d) Aluminio"],
            "respuesta_correcta": "c"
        }
    },
    "Literatura": {
        1: {
            "pregunta": "¿Quién escribió la novela 'Cien años de soledad'?",
            "opciones": ["a) Gabriel García Márquez", "b) Mario Vargas Llosa", "c) Julio Cortázar", "d) Isabel Allende"],
            "respuesta_correcta": "a"
        }
    },
    "Historia": {
        1: {
            "pregunta": "¿En qué año llegó el hombre a la Luna?",
            "opciones": ["a) 1965", "b) 1969", "c) 1972", "d) 1959"],
            "respuesta_correcta": "b"
        }
    },
    "Geografía": {
        1: {
            "pregunta": "¿Cuál es el océano más grande del mundo?",
            "opciones": ["a) Atlántico", "b) Índico", "c) Pacífico", "d) Ártico"],
            "respuesta_correcta": "c"
        }
    }
}

        self.diccionario_preguntas = {
            "Pregunta": "r",
            "Pregunta2": "r2",
            "Pregunta3": "r3"
            }
        self.pregunta_elegida = ""
        self.categoria = ""
        self.terminado = False
        self.rondas = 0
        self.preguntas_realizadas = []

    def elegir_pregunta(self):
        posicion_pregunta = random.choice(list(self.diccionario_preguntas_2[self.categoria]))
        self.preguntas_realizadas.append(posicion_pregunta)
        self.pregunta_elegida = self.diccionario_preguntas_2[self.categoria][posicion_pregunta]

    def elegir_categoria(self):
        categorias = list(self.diccionario_preguntas_2.keys())
        #string_print = list(map(lambda categoria: str(categoria), self.diccionario_preguntas_2))
        print(f"\n\tCategorias:\n")
        for categoria in categorias:
            print(f"\t\t{categoria}\n")
        categoria = input("\n\n\tElige categoria: ")
        self.categoria = categoria.strip().capitalize()
        self.elegir_pregunta()
        print()

    def tablero(self):
        print("\n\tBienvenido a preguntados\n")
        print("\n\tObjetivo: Responde bien 10 rondas seguidas y gana\n")
        if self.categoria == "":
            self.elegir_categoria()
        self.elegir_pregunta()
        print(f"\tPregunta {self.rondas+1}\n")
        pregunta = self.pregunta_elegida["pregunta"]
        print(f"\t{pregunta}\n")
        opciones = self.pregunta_elegida["opciones"]
        for opcion in opciones:
            print(f"\t\t{opcion}")

    #posiblemente lo quite
    def restablecer_tablero(self):
        self.rondas = 0
        self.categoria = ""
        self.preguntas_realizadas = []
        

    def jugar(self):
        system("cls")
        while True:
            if self.terminado == True:
                opcion = input("¿Quieres volver a jugar?\nSi - No\n")
                if opcion.lower() == "s" or opcion.lower() == "si":
                    self.rondas = 0
                    self.categoria = ""
                    self.preguntas_realizadas = []
                    self.terminado = False
                else:
                    print("Hasta luego")
                    break
            else:
                self.tablero()
                valor = input("\n\tIntroduce la letra de tu respuesta: ")
                if valor == 'q':
                    print("Hasta luego")
                    break
                if valor.lower() == self.pregunta_elegida["respuesta_correcta"]:
                    self.rondas = self.rondas + 1
                    if self.rondas == 2:
                        print("HAS GANADO")
                        self.terminado = True
                    else:
                        print("\n\tEs correcto 🙌 Siguiente pregunta ⏭️")
                else:
                    print("No es correcto. Has perdido 😭")
                    self.categoria = ""
                    self.pregunta_elegida = ""
                    self.preguntas_realizadas = []
                    self.rondas = 0
                    self.terminado = True
                        
            
            