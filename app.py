import streamlit as st
from main import generar_respuesta, inicializar_vectorstore

# Configuración de la página 
st.set_page_config(page_title="Asistente Virtual de Juan Pérez", page_icon="🤖")

# Inicializar el vectorstore
@st.cache_resource(show_spinner="Cargando el CV...")
def load_vectorstore():
    return inicializar_vectorstore()

vectorstore = load_vectorstore()

# Interfaz principal
st.title("🤖 Asistente Virtual de Juan Pérez")
st.write("Preguntale lo que quieras sobre su perfil profesional.")

# Estado de la conversación 
if "historial" not in st.session_state:
    st.session_state.historial = []

# Input del usuario 
consulta = st.chat_input("Escribí tu pregunta aquí...")

# Procesamiento de la consulta 
if consulta:
    if consulta.lower() in ["salir", "exit", "quit"]:
        st.session_state.historial = []  # Limpia el historial
        st.markdown("👋 ¡Gracias por visitar el asistente de Juan Pérez! Que tengas un gran día.")
        st.stop() 
    else:
        respuesta = generar_respuesta(consulta, vectorstore)
        st.session_state.historial.append({"consulta": consulta, "respuesta": respuesta})

# Mostrar historial del chat
for intercambio in st.session_state.historial:
    with st.chat_message("🧑‍💼"):
        st.markdown(intercambio["consulta"])
    with st.chat_message("🤖"):
        st.markdown(intercambio["respuesta"])

# Footer
st.markdown("---")
st.markdown("Hecho con 💙 por Ayelén usando LangChain + Streamlit")
st.markdown("[Conectá conmigo en LinkedIn](https://www.linkedin.com/in/-ayelen-alvarez/)")