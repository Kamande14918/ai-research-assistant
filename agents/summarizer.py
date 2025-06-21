from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

def get_summarizer_agent():
    prompt = PromptTemplate.from_template(
        "Summarize the following findings concisely with citations included:\n\n{input}"
    )
    llm = ChatOpenAI(model="gpt-4", temperature=0.3)
    return prompt | llm