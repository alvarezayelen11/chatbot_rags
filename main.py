# Importamos las librerías
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os

# Inicializar modelo de embedding
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Inicializar historial de conversación
memory = ConversationBufferWindowMemory(k=3)

# Inicializar modelo de lenguaje
load_dotenv()
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    google_api_type="aistudio",
    temperature=0.2
)

# Inicializar cadena de conversación con memoria
chat_chain = ConversationChain(llm=llm, memory=memory, verbose=False)

def inicializar_vectorstore():
    persist_directory = "chroma/"
    if os.path.exists(persist_directory):
        print("🔄 Cargando datos previamente procesados...")
        return Chroma(persist_directory=persist_directory, embedding_function=embedding_model)
    else:
        print("📄 Procesando CV por primera vez...")
        loader = PyPDFLoader("hoja_de_vida_juan_perez.pdf")
        documentos = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        documentos_divididos = splitter.split_documents(documentos)
        vectorstore = Chroma.from_documents(documentos_divididos, embedding_model, persist_directory=persist_directory)
        return vectorstore

def generar_respuesta(pregunta, vectorstore):
    retriever = vectorstore.as_retriever()
    documentos = retriever.invoke(pregunta)
    contexto = "\n\n".join([doc.page_content for doc in documentos])

    prompt = f"""
    Actuás como el asistente virtual de Juan Pérez, un profesional cuyo perfil está descripto en su CV.

    Información disponible:
    {contexto}

    Instrucciones:
    1. Si encontrás información relevante en el CV, usala para responder de manera clara y profesional.
    2. Solo si no podés responder con la información disponible, sugerí que se contacten con Juan por mail a juanperez@email.com.
    3. Mantené el mismo idioma de la consulta (español o inglés).
    4. Usá un tono profesional y cordial, como si representaras a Juan en una conversación con un recruiter.

    Pregunta:
    {pregunta}
    """

    respuesta = chat_chain.invoke(prompt)
    return respuesta['response']

# # Bloque de ejecución directa para testing en consola
if __name__ == "__main__":
    vectorstore = inicializar_vectorstore()
    while True:
        pregunta = input("\n👉 Tu pregunta: ")
        if pregunta.lower() in ["salir", "exit", "quit"]:
            break
        respuesta = generar_respuesta(pregunta, vectorstore)
        print(f"\n💡 Respuesta: {respuesta}")
