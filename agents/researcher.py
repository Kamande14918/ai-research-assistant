from tools.search_tools import search_web
from langchain_openai import ChatOpenAI

def get_researcher_agent():
    def agent(input):
        # If input is a dict, extract the query string
        if isinstance(input, dict) and "input" in input:
            query = input["input"]
        else:
            query = input
        result = search_web(query)
        return {"output": result}  # <-- Return as dict!
    return agent
