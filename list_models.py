import os
from dotenv import load_dotenv
load_dotenv()

from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

for m in client.models.list():
    # In tên model và các method hỗ trợ (nếu field tồn tại)
    name = getattr(m, "name", None)
    methods = getattr(m, "supported_generation_methods", None)
    print(name, methods)