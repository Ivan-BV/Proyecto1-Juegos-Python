import random
from os import system
from time import sleep

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

        self.pregunta_elegida = ""
        self.categoria = ""
        self.terminado = False
        self.rondas = 0
        self.preguntas_realizadas = []
        self.input_erroneo = False
        self.respuesta = ""
        self.titulo_ascii = """    ____  ____  ______________  ___   ___________    ____  ____  _____
   / __ \/ __ \/ ____/ ____/ / / / | / /_  __/   |  / __ \/ __ \/ ___/
  / /_/ / /_/ / __/ / / __/ / / /  |/ / / / / /| | / / / / / / /\__ \ 
 / ____/ _, _/ /___/ /_/ / /_/ / /|  / / / / ___ |/ /_/ / /_/ /___/ / 
/_/   /_/ |_/_____/\____/\____/_/ |_/ /_/ /_/  |_/_____/\____//____/  
                                                                      
"""

    def comprobar_respuesta(self):
        if self.respuesta.isalpha() and self.respuesta != r"!\"#\$%&'\(\)\*\+,-\.\/:;<=>\?@\[\\\]\^_`\{\|\}~" and len(self.respuesta) == 1:
            self.input_erroneo = False
            if self.respuesta.lower() == self.pregunta_elegida["respuesta_correcta"]:
                self.rondas = self.rondas + 1
                if self.rondas == 9:
                    print("HAS GANADO")
                    self.terminado = True
                else:
                    print("\n\tEs correcto 🙌 Siguiente pregunta ⏭️")
                    sleep(3)
            else:
                print("\n\tNo es correcto. Has perdido 😭", f"\n\n\tHas llegado hasta la pregunta: {self.rondas+1}")
                self.categoria = ""
                self.pregunta_elegida = ""
                self.preguntas_realizadas = []
                self.rondas = 0
                self.terminado = True
        else:
            self.input_erroneo = True

    def elegir_pregunta(self):
        posicion_pregunta = random.choice(list(self.diccionario_preguntas_2[self.categoria]))
        self.preguntas_realizadas.append(posicion_pregunta)
        self.pregunta_elegida = self.diccionario_preguntas_2[self.categoria][posicion_pregunta]

    def elegir_categoria(self):
        categorias = list(self.diccionario_preguntas_2.keys())
        print(f"\n\tCategorias:\n")
        for categoria in categorias:
            print("\t🔸 ", categoria)
        print("\n\t═════════════════════════════════════════════════")
        categoria = input("\n\tElige categoria: ")
        self.categoria = categoria.capitalize().strip() if categoria.capitalize().strip() in categorias else ""
        if self.categoria == "":
            self.input_erroneo = True
        else:
            self.input_erroneo = False
            

    def tablero(self):
        system("cls")
        print(f"{self.titulo_ascii}")
        print("\t═════════════════════════════════════════════════")
        print("\n\tObjetivo: Responde bien 10 rondas seguidas y gana\n")
        print("\t═════════════════════════════════════════════════")
        if self.input_erroneo == True:
            if self.categoria == "":
                print("\n\t⚠️ Introduce una categoria valida ⚠️")
            else:
                if len(self.respuesta) > 1:
                    print("\n\t⚠️ Introduce solo una letra a la vez ⚠️")
                elif len(self.respuesta) == 0:
                    print("\n\t⚠️ Introduce al menos una letra ⚠️")
                else:
                    print("\n\t⚠️ Introduce una letra valida ⚠️")
        
        if self.categoria == "":
            self.elegir_categoria()
        else:
            #print("\t═════════════════════════════════════════════════")
            self.elegir_pregunta()
            print(f"\n\tPregunta {self.rondas+1}\n")
            pregunta = self.pregunta_elegida["pregunta"]
            print(f"\t{pregunta}\n")
            opciones = self.pregunta_elegida["opciones"]
            for opcion in opciones:
                print(f"\t\t{opcion}")
            print("\n\t═════════════════════════════════════════════════")
        
        
    def jugar(self):
        system("cls")
        print("\n\t\t¡Bienvenido a preguntados!\n")
        while True:
            #Compruebo si quiere volver a empezar, si es afirmativo se reinicia todo
            #en caso contrario sale del bucle volviendo así al menú
            if self.terminado == True:
                opcion = input("\n\t¿Quieres volver a jugar?\n\n\tEscribe s para si, n para no\n\n\t--> ")
                if opcion.lower() == "s" or opcion.lower() == "si":
                    self.rondas = 0
                    self.categoria = ""
                    self.preguntas_realizadas = []
                    self.terminado = False
                else:
                    print("\n\t\t\tHasta luego 👋")
                    break
            else:
                self.tablero()
                if self.pregunta_elegida != "":
                    self.respuesta = input("\n\tIntroduce tu respuesta: ")
                    self.comprobar_respuesta()

                
                        
            
            