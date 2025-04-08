# 🤖 Asistente Virtual de Juan Pérez

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
├── hoja_de_vida_juan_perez.pdf   # CV base para responder preguntas
├── requirements.txt              # Librerías necesarias para el entorno
```

---

## ⚙️ Instalación y ejecución local

1. Cloná el repositorio:
```bash
git clone https://github.com/tu-usuario/chatbot_rags.git
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

## 💡 Características

- Conserva el contexto de las últimas 3 preguntas y respuestas, guardándolas en la memoria conversacional.
- Procesa el documento en PDF y lo convierte en vectores (esta versión se configuró en chunk_size=500 y chunk_overlap=100).
- Está optimizado para responder en **español** e **inglés**.

---

## 📬 Contacto

Creado por [Ayelén Álvarez](https://www.linkedin.com/in/-ayelen-alvarez/)

---

## 📢 Feedback

If you have any comments, please write to me.
