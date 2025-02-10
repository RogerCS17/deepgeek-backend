class LLMModel:
    """Maneja la comunicación con la API de DeepSeek."""

    def __init__(self, chat):
        self.chat = chat

    def get_response(self, prompt_messages):
        return self.chat.get_response(prompt_messages)
