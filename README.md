# 🚗 Asistente Virtual de Educación Vial

## 📌 Descripción
Este proyecto consiste en un chatbot educativo diseñado para ayudar a los usuarios a prepararse para el examen teórico de manejo en Costa Rica.

El sistema responde preguntas relacionadas con:
- Señales de tránsito
- Normas de circulación
- Prioridad de paso
- Seguridad vial
- Conducción defensiva

---

## 🎯 Objetivo académico
Desarrollar un sistema capaz de interpretar preguntas del usuario y responder utilizando una base de conocimiento estructurada.

---

## 🧠 Funcionamiento del Sistema
El chatbot implementa un pipeline básico de procesamiento de lenguaje natural:

1. **Preprocesamiento**
   - Conversión a minúsculas
   - Eliminación de signos
   - Tokenización

2. **Detección de intención**
   - Saludo
   - Pregunta
   - Despedida

3. **Algoritmo de coincidencia**
   - Comparación de palabras clave con patrones

4. **Generación de respuesta**
   - Respuesta dinámica basada en la intención

---

## 🛠️ Tecnologías utilizadas
   -Python
   -JSON
   -Procesamiento de lenguaje natural básico

---

## 📁 Estructura del Proyecto
Chatbot/
│
├── chatbot.py
├── knowledge.json
├── README.md
