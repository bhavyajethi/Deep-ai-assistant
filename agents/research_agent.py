from langchain.tools.tavily_search import TavilySearchResults
import os
from dotenv import load_dotenv

load_dotenv()

def research_node(query):
    tool = TavilySearchResults(k=5)
    results = tool.run(query)
    return {"query":query, "research_data": results}