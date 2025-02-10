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

    respuestas_usuario = request.json

    prompt_messages = prompt_generator.generate_prompt(respuestas_usuario)
    chat = DeepSeekChat(api_key=api_key)
    chat_model = LLMModel(chat)
    response = chat_model.get_response(prompt_messages)

    return jsonify({"result": response})
