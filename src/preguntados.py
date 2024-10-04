import random

class Preguntados:
    def __init__(self):
        self.diccionario_preguntas = {
            "Pregunta": "Respuesta",
            "Pregunta2": "Respuesta2",
            "Pregunta3": "Respuesta3"
            }
        self.pregunta = random.choices(list(self.diccionario_preguntas))

        self.terminado = False

    def tablero():
        print("\nBienvenido a preguntados\n")
        print()

    def jugar(self):
        while True:
            if self.terminado == True:
                opcion = input("¿Quieres volver a jugar?\nSi - No\n")
                if opcion.lower() == "s" or opcion.lower() == "si":
                    self.terminado = False
                    self.pregunta = random.choices(list(self.diccionario_preguntas))
                else:
                    break
            else:
                print(self.diccionario_preguntas.values())
                print(self.pregunta)
                valor = input("\nIntroduce respuesta: ")
                if valor == 'q':
                    print("Hasta luego")
                    break
                for respuesta in self.diccionario_preguntas.values():
                    print(respuesta)
                    if valor == respuesta:
                        print("Es correcto")
                        self.terminado = True
                        break
                    else:
                        print("No es correcto")
            
            