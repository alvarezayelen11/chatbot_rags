# 🤖 Asistente Virtual de Juan Pérez

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Framework-black)
![Google Gemini](https://img.shields.io/badge/Google-Gemini_AI-orange?logo=google)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-yellow?logo=huggingface)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-purple)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)

Este proyecto es un asistente virtual construido con **LangChain**, **Google Gemini AI** y **Streamlit** que responde preguntas sobre la hoja de vida (CV) de Juan Pérez. Permite interactuar con su perfil profesional a través de lenguaje natural.

---

## 🌐 Tecnologías utilizadas

- **Python 3.11**
- **LangChain**: para orquestar el flujo entre el modelo LLM, la memoria y los documentos.
- **Google Generative AI (Gemini)**: como modelo de lenguaje principal.
- **Hugging Face Embeddings**: para convertir el documento PDF en vectores.
- **ChromaDB**: para almacenamiento y recuperación de embeddings.
- **Streamlit**: como interfaz.

---

## 📁 Estructura del proyecto

```
chatbot_rags/
├── .env.example                  # Plantilla de referencia para .env
├── .gitignore                    # Lista de archivos y carpetas a ignorar
├── app.py                        # Interfaz Streamlit del chatbot
├── main.py                       # Lógica del chatbot: embeddings, prompt, memoria, etc.
├── hoja_de_vida_juan_perez.pdf  # CV base para responder preguntas
├── requirements.txt              # Librerías necesarias para el entorno
├── demo_chatbot.gif              # Vista previa del chatbot en funcionamiento
```

---

## ⚙️ Instalación y ejecución local

1. Cloná el repositorio:
```bash
git clone https://github.com/alvarezayelen11/chatbot_rags.git
cd chatbot_rags
```

2. Creá y activá un entorno virtual:
```bash
python -m venv env_rags
env_rags\Scripts\activate     # En Windows
```

3. Instalá las dependencias:
```bash
pip install -r requirements.txt
```

4. Agregá tu clave en un archivo `.env`:
```
GOOGLE_API_KEY=tu_clave_de_google
```

5. Ejecutá el proyecto:
```bash
streamlit run app.py
```

---

## 🎥 Demo 

![Demo](https://raw.githubusercontent.com/alvarezayelen11/chatbot_rags/master/demo_chatbot.gif)

---

## 🧑‍💻 Autor

[Ayelén Álvarez](https://www.linkedin.com/in/-ayelen-alvarez/)

---

## ✉️ Feedback

Si tenés algún comentario o sugerencia sobre el proyecto, no dudes en escribirme.
