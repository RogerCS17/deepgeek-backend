from abc import ABC, abstractmethod


class LLMModel:
    """Maneja la comunicación con la API de DeepSeek."""

    def __init__(self, chat):
        self.chat = chat

    def get_response(self, prompt_messages):
        return self.chat.get_response(prompt_messages)

class ImageModel(ABC):
    @abstractmethod
    def get_response(self, prompt: str):
        pass

class DalleImageModel(ImageModel):
    def __init__(self, client, model="dall-e-2"):
        self.client = client
        self.model = model

    def get_response(self, prompt):
        try:
            response = self.client.images.generate(
                model=self.model, prompt=prompt, size="512x512", quality="standard", n=1
            )
            return response.data[0].url
        except Exception as e:
            print(f"Error al generar la imagen: {e}")
            return None