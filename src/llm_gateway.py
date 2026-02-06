import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

class LLMGateway:
    def __init__(self, model: str, mock: bool = False):
        self.mock = mock
        self.model_name = model

        if not mock:
            self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY")
            )

    def generate(self, prompt: str) -> str:
        if self.mock:
            return "Mock response generated for testing purposes."

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt
        )

        return response.text
