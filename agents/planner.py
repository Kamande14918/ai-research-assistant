from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Clarifies query before decomposition
def get_planner_agent():
    prompt = PromptTemplate.from_template(
        """
        You are a planning assistant. First ask clarifying questions about this user input:
        {input}

        Then break the refined query into 3-5 concrete research tasks.
        """
    )
    llm = ChatOpenAI(model="gpt-4", temperature=0)
    return prompt | llm