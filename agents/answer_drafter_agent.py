from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
import json

load_dotenv()

def draft_answer_node(data):
    # Initialize the LLM with the specified model and temperature
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-001", temperature=0.5, max_tokens = 3000) 
    
    # Extract and stringify the research_data from input
    research_data = data.get("research_data", {})
    stringified_data = json.dumps(research_data)  
    
    # Create prompt template with proper variable placeholder
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful research assistant."),
        ("user", "Based on the following research data, write a concise, informative answer:\n{research_data}")
    ])
    
    # Create processing chain
    chain = prompt | llm
    
    # Invoke chain with properly named input
    response = chain.invoke({"research_data": stringified_data})
    
    # Return the text content of the response
    return {"final_answer": response.content}