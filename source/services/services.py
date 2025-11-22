import os
import google.generativeai as genai
from dotenv import (
    load_dotenv,
)

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("ERRO: A chave GOOGLE_API_KEY não foi encontrada no arquivo .env")
else:
    genai.configure(api_key=api_key)


def get_ai_response(question):
    try:

        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(question)

        return response.text

    except Exception as e:
        print(f"Erro no Gemini: {e}")
        return "Desculpe, tive um problema ao processar sua pergunta com o Gemini."
