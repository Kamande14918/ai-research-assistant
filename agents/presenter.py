from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

def get_presenter_agent():
    prompt =PromptTemplate.from_template(
    """
    Present a final, academically formatted research report from the refined summary:
    {input}
    """
    )
    llm = ChatOpenAI(model="gpt-4", temperature=0.3)
    return prompt | llm