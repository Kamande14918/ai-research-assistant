# Optional multiple perspectives
from langchain_openai import ChatOpenAI

def get_expert(name):
    system=f"You are an expert {name}. Provide brief commentary on the topic."
    return ChatOpenAI(model="gpt-4", temperature=0.4).bind(system_message=system)