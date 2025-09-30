from google import genai
from google.genai import types
from datatypes import Response

class AIModel:
    def __init__(self, uploaded_resume):
        # REMEMBER TO ADD YOUR GEMINI API KEY HERE
        self.client = genai.Client(api_key="")
        self.model = "gemini-2.5-flash"
        self.resume = self.client.files.upload(
            # You can pass a path or a file-like object here
            file=uploaded_resume,
            config=dict(mime_type="application/pdf"),
        )

    def generateResponse(self, prompt):
        if not prompt:
            raise ValueError("prompt is not defined")
        return self.client.models.generate_content(
            model=self.model,
            contents=[self.resume, prompt],
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0),
                response_mime_type="application/json",
                response_schema=Response,
                temperature=0
            ),
        )
