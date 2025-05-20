import os
import google.generativeai as genai

genai.configure.api_key = os.getenv("GOOGLE_API_KEY")
model = genai.GenerativeModel("gemini-pro")

def compare(topic1, topic2):
    prompt = f"Compare and contrast {topic1} and {topic2}."
    response = model.generate_content(prompt)
    return response.text