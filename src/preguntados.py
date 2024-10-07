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
        },
        5: {
            "pregunta": "¿Qué órgano humano produce insulina?",
            "opciones": ["a) Corazón", "b) Riñón", "c) Páncreas", "d) Hígado"],
            "respuesta_correcta": "c"
        },
        6: {
            "pregunta": "¿Qué tipo de célula no tiene núcleo?",
            "opciones": ["a) Célula vegetal", "b) Célula eucariota", "c) Célula procariota", "d) Célula animal"],
            "respuesta_correcta": "c"
        },
        7: {
            "pregunta": "¿Qué partícula subatómica tiene carga negativa?",
            "opciones": ["a) Protón", "b) Neutrón", "c) Electrón", "d) Fotón"],
            "respuesta_correcta": "c"
        },
        8: {
            "pregunta": "¿Cuál es el elemento más abundante en el universo?",
            "opciones": ["a) Hidrógeno", "b) Oxígeno", "c) Carbono", "d) Nitrógeno"],
            "respuesta_correcta": "a"
        },
        9: {
            "pregunta": "¿Qué órgano humano es el responsable de filtrar la sangre?",
            "opciones": ["a) Hígado", "b) Corazón", "c) Riñón", "d) Pulmones"],
            "respuesta_correcta": "c"
        },
        10: {
            "pregunta": "¿Qué proceso convierte el azúcar en alcohol?",
            "opciones": ["a) Evaporación", "b) Oxidación", "c) Fermentación", "d) Destilación"],
            "respuesta_correcta": "c"
        }
    },
    
    "Historia": {
        1: {
            "pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
            "opciones": ["a) 1914", "b) 1939", "c) 1945", "d) 1929"],
            "respuesta_correcta": "b"
        },
        2: {
            "pregunta": "¿Quién fue el primer presidente de los Estados Unidos?",
            "opciones": ["a) Abraham Lincoln", "b) George Washington", "c) Thomas Jefferson", "d) John Adams"],
            "respuesta_correcta": "b"
        },
        3: {
            "pregunta": "¿Cuál fue la civilización que construyó las pirámides de Egipto?",
            "opciones": ["a) Griegos", "b) Romanos", "c) Egipcios", "d) Persas"],
            "respuesta_correcta": "c"
        },
        4: {
            "pregunta": "¿En qué país se originó la Revolución Industrial?",
            "opciones": ["a) Francia", "b) Alemania", "c) Reino Unido", "d) Estados Unidos"],
            "respuesta_correcta": "c"
        },
        5: {
            "pregunta": "¿Quién pintó la Mona Lisa?",
            "opciones": ["a) Pablo Picasso", "b) Vincent van Gogh", "c) Leonardo da Vinci", "d) Miguel Ángel"],
            "respuesta_correcta": "c"
        },
        6: {
            "pregunta": "¿Qué emperador romano legalizó el cristianismo?",
            "opciones": ["a) Nerón", "b) Julio César", "c) Constantino", "d) Augusto"],
            "respuesta_correcta": "c"
        },
        7: {
            "pregunta": "¿Quién lideró la independencia de la India en 1947?",
            "opciones": ["a) Nelson Mandela", "b) Mahatma Gandhi", "c) Jawaharlal Nehru", "d) Winston Churchill"],
            "respuesta_correcta": "b"
        },
        8: {
            "pregunta": "¿En qué año cayó el muro de Berlín?",
            "opciones": ["a) 1985", "b) 1989", "c) 1991", "d) 1979"],
            "respuesta_correcta": "b"
        },
        9: {
            "pregunta": "¿Quién fue el conquistador que derrotó al Imperio Azteca?",
            "opciones": ["a) Cristóbal Colón", "b) Hernán Cortés", "c) Francisco Pizarro", "d) Pedro de Alvarado"],
            "respuesta_correcta": "b"
        },
        10: {
            "pregunta": "¿Qué tratado puso fin a la Primera Guerra Mundial?",
            "opciones": ["a) Tratado de París", "b) Tratado de Tordesillas", "c) Tratado de Versalles", "d) Paz de Westfalia"],
            "respuesta_correcta": "c"
        }
    },
    
    "Geografía": {
        1: {
            "pregunta": "¿Cuál es el océano más grande del mundo?",
            "opciones": ["a) Atlántico", "b) Índico", "c) Pacífico", "d) Ártico"],
            "respuesta_correcta": "c"
        },
        2: {
            "pregunta": "¿Cuál es la capital de Canadá?",
            "opciones": ["a) Ottawa", "b) Toronto", "c) Vancouver", "d) Montreal"],
            "respuesta_correcta": "a"
        },
        3: {
            "pregunta": "¿Cuál es el país más grande del mundo?",
            "opciones": ["a) China", "b) Estados Unidos", "c) Canadá", "d) Rusia"],
            "respuesta_correcta": "d"
        },
        4: {
            "pregunta": "¿Cuál es el río más largo del mundo?",
            "opciones": ["a) Amazonas", "b) Nilo", "c) Yangtsé", "d) Misisipi"],
            "respuesta_correcta": "b"
        },
        5: {
            "pregunta": "¿En qué continente se encuentra el desierto del Sahara?",
            "opciones": ["a) Asia", "b) África", "c) América del Sur", "d) Australia"],
            "respuesta_correcta": "b"
        },
        6: {
            "pregunta": "¿Cuál es la montaña más alta del mundo?",
            "opciones": ["a) K2", "b) Kilimanjaro", "c) Monte Everest", "d) Aconcagua"],
            "respuesta_correcta": "c"
        },
        7: {
            "pregunta": "¿Qué país tiene la mayor cantidad de islas?",
            "opciones": ["a) Noruega", "b) Suecia", "c) Indonesia", "d) Japón"],
            "respuesta_correcta": "b"
        },
        8: {
            "pregunta": "¿Cuál es el país más poblado del mundo?",
            "opciones": ["a) India", "b) Estados Unidos", "c) China", "d) Rusia"],
            "respuesta_correcta": "c"
        },
        9: {
            "pregunta": "¿Cuál es la capital de Australia?",
            "opciones": ["a) Sídney", "b) Melbourne", "c) Canberra", "d) Brisbane"],
            "respuesta_correcta": "c"
        },
        10: {
            "pregunta": "¿Qué país tiene forma de bota?",
            "opciones": ["a) España", "b) Grecia", "c) Italia", "d) Portugal"],
            "respuesta_correcta": "c"
        }
    },
    
    "Literatura": {
        1: {
            "pregunta": "¿Quién escribió 'Cien años de soledad'?",
            "opciones": ["a) Gabriel García Márquez", "b) Mario Vargas Llosa", "c) Julio Cortázar", "d) Isabel Allende"],
            "respuesta_correcta": "a"
        },
        2: {
            "pregunta": "¿Quién es el autor de 'Don Quijote de la Mancha'?",
            "opciones": ["a) Lope de Vega", "b) Francisco de Quevedo", "c) Miguel de Cervantes", "d) Garcilaso de la Vega"],
            "respuesta_correcta": "c"
        },
        3: {
            "pregunta": "¿Qué novela comienza con la frase 'Es el mejor de los tiempos, es el peor de los tiempos'?",
            "opciones": ["a) Orgullo y Prejuicio", "b) Historia de dos ciudades", "c) Matar a un ruiseñor", "d) Los miserables"],
            "respuesta_correcta": "b"
        },
        4: {
            "pregunta": "¿Qué poeta escribió 'Las flores del mal'?",
            "opciones": ["a) Charles Baudelaire", "b) Arthur Rimbaud", "c) Paul Verlaine", "d) Stéphane Mallarmé"],
            "respuesta_correcta": "a"
        },
        5: {
            "pregunta": "¿Qué obra de Shakespeare presenta a los personajes de Romeo y Julieta?",
            "opciones": ["a) Hamlet", "b) Macbeth", "c) Otelo", "d) Romeo y Julieta"],
            "respuesta_correcta": "d"
        },
        6: {
            "pregunta": "¿Quién escribió la trilogía 'El Señor de los Anillos'?",
            "opciones": ["a) J.K. Rowling", "b) J.R.R. Tolkien", "c) George R.R. Martin", "d) C.S. Lewis"],
            "respuesta_correcta": "b"
        },
        7: {
            "pregunta": "¿En qué país nació el escritor Jorge Luis Borges?",
            "opciones": ["a) Chile", "b) España", "c) Argentina", "d) México"],
            "respuesta_correcta": "c"
        },
        8: {
            "pregunta": "¿Quién escribió '1984'?",
            "opciones": ["a) Aldous Huxley", "b) Ray Bradbury", "c) George Orwell", "d) Isaac Asimov"],
            "respuesta_correcta": "c"
        },
        9: {
            "pregunta": "¿En qué novela aparece el personaje de Jay Gatsby?",
            "opciones": ["a) El gran Gatsby", "b) Matar a un ruiseñor", "c) El guardián entre el centeno", "d) Anna Karenina"],
            "respuesta_correcta": "a"
        },
        10: {
            "pregunta": "¿Qué autor escribió 'La Odisea'?",
            "opciones": ["a) Sófocles", "b) Virgilio", "c) Homero", "d) Hesíodo"],
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

                
                        
            
            