from google import genai
import os

print("KEY FOUND:", bool(os.getenv("GEMINI_API_KEY")))

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-1.0-pro",
    contents="Say hello in one word"
)

print(response.text)
