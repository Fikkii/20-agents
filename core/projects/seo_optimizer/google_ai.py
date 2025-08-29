import google.generativeai as genai
from crewai.llms.base_llm import BaseLLM   # ✅ correct import
from crewai.tools import tool
from typing import Any

# -------------------------
# Gemini wrapper for CrewAI
# -------------------------
class GeminiLLM(BaseLLM):
    def __init__(self, api_key: str, model: str = "gemini-1.5-flash", temperature: float = 0.1):
        super().__init__(model=model)
        self.api_key = api_key
        self.model = model
        self.temperature = temperature

        # Configure Gemini client
        genai.configure(api_key=self.api_key)
        self.client = genai.GenerativeModel(self.model)

        # 👇 Add this attribute
        self.supports_function_calling = True


    def _generate(self, prompt: Any) -> str:
        """Internal call to Gemini, normalize CrewAI input"""

        # If CrewAI passes dicts like {"role": "user", "content": "..."}
        if isinstance(prompt, dict) and "content" in prompt:
            prompt_text = prompt["content"]

        # If CrewAI passes list of messages
        elif isinstance(prompt, list):
            # join all role/content into a string (simple fallback)
            prompt_text = "\n".join(
                f"{m.get('role','user')}: {m.get('content','')}" for m in prompt
            )

        else:
            # normal string
            prompt_text = str(prompt)

        response = self.client.generate_content(
            [{"role": "user", "parts": [{"text": prompt_text}]}],
            generation_config={"temperature": self.temperature}
        )

        return response.text

    # CrewAI expects these
    def predict(self, prompt: str, **kwargs: Any) -> str:
        return self._generate(prompt)

    def call(self, prompt: str, **kwargs: Any) -> str:
        return self._generate(prompt)


gemini_llm = GeminiLLM(
    api_key="AIzaSyBu9dpat9hkVBotrANSYA7fZkXD9XJlg1o",   # <-- Replace with your real API key
    model="gemini-1.5-flash",
    temperature=0.1
)

