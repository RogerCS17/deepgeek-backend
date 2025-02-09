from flask import Blueprint, jsonify, request
from app.core.config import ConfigLoader
from app.models.llm_model import LLMModel
from app.services.chat.chat_model import DeepSeekChat
from app.services.prompts import PromptGenerator

comic_bp = Blueprint('comic', __name__)


@comic_bp.route('/analyze', methods=['POST'])
def analyze_hero():
    api_key = ConfigLoader.load_api_key()
    prompt_generator = PromptGenerator()

    respuestas_usuario = {
        "editorial": "Marvel",
        "respuesta_1": "Mi fuerza física y resistencia.",
        "respuesta_2": "Intento razonar con mi enemigo primero.",
        "respuesta_3": "Poderes sobrenaturales o tecnología avanzada.",
        "respuesta_4": "Los que usan magia oscura o fuerzas desconocidas.",
        "respuesta_5": "Teletransportándome o usando portales.",
        "respuesta_6": "Dudar de mí mismo en momentos clave.",
        "respuesta_7": "Un bromista con un gran corazón.",
        "respuesta_8": "Una sede de justicia y paz.",
        "respuesta_9": "Rojo y azul con detalles llamativos.",
        "respuesta_10": "Analizar qué salió mal para mejorar en el futuro.",
    }

    prompt_messages = prompt_generator.generate_prompt(respuestas_usuario)
    chat = DeepSeekChat(api_key=api_key)
    chat_model = LLMModel(chat)
    response = chat_model.get_response(prompt_messages)

    return jsonify({"result": response})
