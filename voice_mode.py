import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv

# ── Setup ─────────────────────────────────────────────────────────────
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))          # ← correct way
model = genai.GenerativeModel("gemini-1.5-flash-001")

# ── Helpers ───────────────────────────────────────────────────────────
def listen_and_transcribe():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤  Speak now…")
        audio = recognizer.listen(source)       # ← use recognizer.listen
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError as e:
        return f"Speech-recognition error: {e}"

def speak_output(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# ── Voice-chat loop ───────────────────────────────────────────────────
def voice_chat():
    query = listen_and_transcribe()
    if not query:
        print("No speech detected.")
        return

    print(f"🗣  You said: {query}")
    response = model.generate_content(query)
    answer = response.text.strip() if response and response.text else "No answer generated."
    print(f"🤖 Gemini says: {answer}")
    speak_output(answer)

# ── Run once ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    voice_chat()
