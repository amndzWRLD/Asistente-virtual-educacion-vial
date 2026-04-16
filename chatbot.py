import json
import re


def cargar_base_conocimiento(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)



def preprocesar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)  
    tokens = texto.split()
    return tokens



def detectar_intencion(tokens):
    if "hola" in tokens or "buenas" in tokens:
        return "saludo"

    if "gracias" in tokens or "adios" in tokens:
        return "despedida"

    if "que" in tokens or "como" in tokens or "cuando" in tokens:
        return "pregunta"

    return "desconocido"



def calcular_coincidencia(tokens_usuario, patterns):
    coincidencias = 0

    texto_patterns = " ".join(patterns)

    for token in tokens_usuario:
        if token in texto_patterns:
            coincidencias += 1

    return coincidencias




def buscar_mejor_respuesta(tokens, knowledge_base):
    mejor_respuesta = None
    mayor_coincidencia = 0

    for tema in knowledge_base:
        for entrada in knowledge_base[tema]:
            patterns = entrada["patterns"]
            respuesta = entrada["answer"]

            score = calcular_coincidencia(tokens, patterns)

            if score > mayor_coincidencia:
                mayor_coincidencia = score
                mejor_respuesta = respuesta

    return mejor_respuesta



def generar_respuesta(intencion, respuesta_base):

    if intencion == "saludo":
        return "Hola, soy tu asistente de manejo. ¿En qué puedo ayudarte?"

    if intencion == "despedida":
        return "Con gusto, ¡hasta luego!"

    if intencion == "pregunta":
        if respuesta_base:
            return f" Esto fue lo que encontré:\n{respuesta_base}"
        else:
            return "No encontré información sobre eso, intenta preguntar diferente."

    return "No entendí tu mensaje "



def chatbot():
    knowledge_base = cargar_base_conocimiento("knowledge.json")

    print("Asistente de Examen de Manejo (Costa Rica)")
    print("Escribe 'salir' para terminar\n")

    while True:
        usuario = input("Tú: ")

        if usuario.lower() == "salir":
            print("Bot: ¡Hasta luego!")
            break

        tokens = preprocesar_texto(usuario)
        intencion = detectar_intencion(tokens)
        respuesta_base = buscar_mejor_respuesta(tokens, knowledge_base)
        respuesta_final = generar_respuesta(intencion, respuesta_base)

        print("Bot:", respuesta_final)



if __name__ == "__main__":
    chatbot()