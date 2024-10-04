class Preguntados():
    def __init__(self):
        self.diccionario_preguntas = {"Pregunta": "Respuesta"}

    def jugar(self):
        while True:
            print(self.diccionario_preguntas[0])
            valor = print("Introduce respuesta: ")
            if valor == self.diccionario_preguntas[0]:
                print("Es correcto")
            else:
                print("Es nada")