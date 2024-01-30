import openai
import os
from dotenv import load_dotenv

load_dotenv()

def obtener_respuesta_binaria(numero):
    api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = api_key

    # Construye el prompt para la API
    prompt = f"Transforma el número {numero} a su representación binaria."

    # Realiza una solicitud a la API utilizando el endpoint específico para modelos de chat
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Utiliza el modelo gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "Eres el Dr. Math, un renombrado matemático puro especializado en teoría de números. "},
            {"role": "user", "content": prompt}
        ]
    )

    # Extrae y devuelve la respuesta generada
    return response['choices'][0]['message']['content'].strip()

def main():
    # Solicita al usuario ingresar un número
    numero = input("Ingrese un número: ")

    try:
        # Convierte el número a su representación binaria
        respuesta_binaria = obtener_respuesta_binaria(numero)

        # Imprime la respuesta
        print(f"El número binario correspondiente es: {respuesta_binaria}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

