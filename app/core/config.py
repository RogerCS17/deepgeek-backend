import os
from dotenv import load_dotenv


class ConfigLoader:
    """Carga la configuración desde las variables de entorno."""

    @staticmethod
    def load_api_key():
        load_dotenv()
        return os.getenv("API_KEY")
