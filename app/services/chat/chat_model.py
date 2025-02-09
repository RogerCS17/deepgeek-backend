from abc import ABC, abstractmethod
from langchain_deepseek import ChatDeepSeek


class Chat(ABC):
    """Interfaz para cualquier modelo de chat."""

    @abstractmethod
    def get_response(self, prompt_messages: str) -> str:
        pass


class DeepSeekChat(Chat):
    """Implementación concreta del chat usando DeepSeek."""

    def __init__(self, api_key: str, model: str = "deepseek-chat"):
        self.chat = ChatDeepSeek(api_key=api_key, model=model)

    def get_response(self, prompt_messages: str) -> str:
        return self.chat.invoke(prompt_messages).content
