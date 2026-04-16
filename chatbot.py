import json
import re


IDENTIDAD = {
    "nombre": "V.I.A.L",
    "descripcion": "Vehicular Intelligent Assistant for Learning",
    "personalidad": "preciso, analítico y confiable",
    "tono": "claro, directo y educativo",

    "saludo_inicial": """Inicializando sistema V.I.A.L... 

Hola. Soy V.I.A.L, tu asistente inteligente de educación vial.
Estoy diseñado para ayudarte a comprender las normas de tránsito y prepararte para tu examen de manejo en Costa Rica.

Puedes hacerme preguntas en cualquier momento.""",

    "respuesta_intro": "Procesando consulta...\n\nResultado:",

    "no_entendido": """No se encontró una coincidencia clara en la base de conocimiento.

Te recomiendo reformular la pregunta o utilizar términos relacionados con normas de tránsito.""",

    "despedida": """Sesión finalizada.

Recuerda: una conducción segura comienza con el conocimiento.
Éxitos en tu examen 🚦"""
}



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
        return IDENTIDAD["saludo_inicial"]

    if intencion == "despedida":
        return IDENTIDAD["despedida"]

    if intencion == "pregunta":
        if respuesta_base:
            return f"{IDENTIDAD['respuesta_intro']}\n{respuesta_base}"
        else:
            return IDENTIDAD["no_entendido"]

    return IDENTIDAD["no_entendido"]



def chatbot():
    knowledge_base = cargar_base_conocimiento("knowledge.json")

    print(f"{IDENTIDAD['nombre']} — {IDENTIDAD['descripcion']}")
    print(f"Modo: {IDENTIDAD['personalidad']} | Tono: {IDENTIDAD['tono']}\n")
    print(IDENTIDAD["saludo_inicial"])
    print("\nEscribe 'salir' para terminar\n")

    while True:
        usuario = input("Tú: ")

        if usuario.lower() == "salir":
            print("Bot:", IDENTIDAD["despedida"])
            break

        tokens = preprocesar_texto(usuario)
        intencion = detectar_intencion(tokens)
        respuesta_base = buscar_mejor_respuesta(tokens, knowledge_base)
        respuesta_final = generar_respuesta(intencion, respuesta_base)

        print("Bot:", respuesta_final)



if __name__ == "__main__":
    chatbot()