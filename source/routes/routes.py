from flask import Blueprint, request, jsonify

from source.services.services import get_ai_response

router = Blueprint("router", __name__)


@router.route("/", methods=["GET"])
def hello():
    return jsonify({"message": "API funcionando corretamente!"})


@router.route("/api/ask", methods=["POST"])
def ask():
    """
    Esperado: {"topic": "S3 Buckets"}
    """
    data = request.get_json()

    if not data or "topic" not in data:
        return (
            jsonify(
                {
                    "error": "Por favor, envie o campo 'topic' no JSON. Ex: {'topic': 'Kubernetes'}"
                }
            ),
            400,
        )

    user_topic = data["topic"]

    prompt_context = f"""
    Aja como um Professor Sênior de Cloud Computing (Computação em Nuvem) universitário.
    Seu objetivo é ensinar o aluno sobre o seguinte tópico: '{user_topic}'.

    Por favor, estruture sua resposta da seguinte maneira didática:
    1. 🎓 **Definição Simples**: Explique o que é isso em termos fáceis (como se explicasse para um iniciante).
    2. 🏢 **Analogia do Mundo Real**: Use uma metáfora do dia a dia (sem ser técnica) para ilustrar o conceito.
    3. ☁️ **Exemplo Prático na Nuvem**: Cite como esse recurso se chama ou é usado
    nas principais nuvens (AWS, Azure ou Google Cloud).
    4. 💼 **Por que usar?**: Explique qual problema de negócio isso resolve.

    Mantenha o tom encorajador e técnico na medida certa.
    """

    ai_answer = get_ai_response(prompt_context)

    return jsonify({"response": ai_answer})
