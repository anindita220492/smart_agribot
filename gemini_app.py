

from vertexai.language_models import ChatModel
import vertexai

def ask_gemini(question: str, project_id: str, location: str = "us-central1") -> str:
    vertexai.init(project=project_id, location=location)
    chat_model = ChatModel.from_pretrained("chat-bison")
    chat = chat_model.start_chat()
    response = chat.send_message(question)
    return response.text
