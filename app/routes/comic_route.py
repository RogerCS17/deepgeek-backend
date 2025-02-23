from flask import Blueprint, jsonify, request
from openai import OpenAI
from app.core.config import ConfigLoader
from app.models.model import LLMModel, DalleImageModel
from app.services.chat.chat_model import DeepSeekChat
from app.services.prompts import PromptGenerator, PromptImageGenerator

comic_bp = Blueprint('comic', __name__, url_prefix="/api/comic")


@comic_bp.route('/analyze', methods=['POST'])
def analyze_hero():
    dict_api_key = ConfigLoader.load_api_key()
    api_key_deepseek, api_key_gpt = dict_api_key.values()

    deepseek_chat = DeepSeekChat(api_key=api_key_deepseek)
    gpt_client = OpenAI(api_key=api_key_gpt)

    chat_model = LLMModel(deepseek_chat)
    dalle_model = DalleImageModel(client=gpt_client)

    response_user = request.json

    prompt_messages = PromptGenerator.generate_prompt(response_user)

    response_deepseek = chat_model.get_response(prompt_messages)
    superhero = response_deepseek.split(":")[0]
    print(superhero)
    prompt_image = PromptImageGenerator.generate_prompt(response_user["editorial"], superhero)
    response_gpt = dalle_model.get_response(prompt=prompt_image)

    return jsonify({"result": response_deepseek, "url_image": response_gpt})
