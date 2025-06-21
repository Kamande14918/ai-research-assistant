from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

def get_critic_agent():
    def agent(state):
        output = state["output"]
        improvement_count = state.get("improvement_count", 0)
        # Your logic to decide if improvement is needed
        if "improve" in output.lower():
            improvement_count += 1
        # Return the updated state
        return {
            **state,
            "improvement_count": improvement_count,
            # Optionally update "output" if Critic modifies it
        }
    return agent