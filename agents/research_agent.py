import os
import requests
import google.generativeai as genai
from dotenv import load_dotenv

# Load keys from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash-001")

# Serper.dev setup
SERPER_URL = "https://google.serper.dev/search"
HEADERS = {
    "X-API-KEY": SERPER_API_KEY,
    "Content-Type": "application/json"
}

def fetch_sources(query, max_links=3):
    """Get top sources from Serper.dev API"""
    try:
        payload = {
            "q": query
        }
        res = requests.post(SERPER_URL, headers=HEADERS, json=payload)
        results = res.json()

        links = []
        for item in results.get("news", []) + results.get("organic", []):
            if "link" in item:
                links.append(item["link"])
            if len(links) >= max_links:
                break

        return links

    except Exception as e:
        print(f"❌ Serper error: {e}")
        return []

def research_node(query):
    print(f"📥 Query received: {query}")

    try:
        # Step 1: Gemini answer
        prompt = f"""
You are a helpful AI assistant. Write a well-researched, concise, and accurate answer to the following:

{query}

Make it easy to understand and factual.
"""
        response = model.generate_content(prompt)
        final_answer = response.text.strip() if response and response.text else "No answer generated"
        print("✅ Gemini answer ready.")

        # Step 2: Serper sources
        sources = fetch_sources(query)
        print(f"🔗 Sources found: {len(sources)}")

        return {
            "query": query,
            "gemini_answer": final_answer,
            "sources": sources
        }

    except Exception as e:
        print(f"❌ Error: {e}")
        return {
            "query": query,
            "gemini_answer": f"Error: {str(e)}",
            "sources": []
        }
