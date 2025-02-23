from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)


class PromptGenerator:
    """Genera el prompt basado en las respuestas del usuario."""
    @staticmethod
    def generate_prompt(respuestas: dict):
        system_prompt = """
        Eres un experto en comics de la editorial {editorial}. 
        Eres capaz de analizar las respuestas y determinar qué héroe encaja mejor.
        Finalmente siempre deberás responder primero con el nombre del personaje separarlo por ":" y continuar con 
        una breve pero poderosa descripción.
        """
        human_prompt = """
        ¿Cuál es tu mayor fortaleza? Respuesta: {respuesta_1}
        ¿Cómo enfrentas una amenaza? Respuesta: {respuesta_2}
        ¿Cuál es tu estilo de combate? Respuesta: {respuesta_3}
        ¿Qué tipo de enemigo te molesta más? Respuesta: {respuesta_4}
        ¿Cómo prefieres moverte por la ciudad? Respuesta: {respuesta_5}
        ¿Cuál es tu mayor debilidad? Respuesta: {respuesta_6}
        ¿Cómo te describirían tus amigos? Respuesta: {respuesta_7}
        ¿Cuál sería tu base de operaciones ideal? Respuesta: {respuesta_8}
        ¿Qué color te representa mejor? Respuesta: {respuesta_9}
        ¿Qué harías después de una victoria? Respuesta: {respuesta_10}
        """

        system_message = SystemMessagePromptTemplate.from_template(system_prompt)
        human_message = HumanMessagePromptTemplate.from_template(human_prompt)
        chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])

        return chat_prompt.format_messages(**respuestas)

class PromptImageGenerator:
    """Genera el prompt para generar la imagen de un superhéroe"""
    @staticmethod
    def generate_prompt(editorial, superheroe):
        return f"""
        Crea una versión alternativa de {superheroe} de la editorial {editorial} con un traje innovador, nuevos patrones y materiales avanzados. Puede tener colores diferentes y un diseño más dinámico. La escena debe ser épica, con un fondo de metrópolis futurista, dimensión mística o campo de batalla intergaláctico. Sin texto ni símbolos reconocibles.
        """.strip()