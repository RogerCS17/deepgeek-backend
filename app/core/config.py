import os
from dotenv import load_dotenv


class ConfigLoader:
    """Carga la configuración desde las variables de entorno."""

    @staticmethod
    def load_api_key():
        load_dotenv()
        return {"Deepseek": os.getenv("API_KEY_DEEPSEEK"), "GPT": os.getenv("API_KEY_GPT")}
