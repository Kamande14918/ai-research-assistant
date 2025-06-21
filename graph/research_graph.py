from typing import TypedDict
from langgraph.graph import StateGraph
from agents import planner, researcher, summarizer, critic, presenter

class ResearchState(TypedDict):
    input: str
    output: str
    improvement_count: int  # <-- add this

def build_graph():
    builder = StateGraph(state_schema=ResearchState)

    builder.add_node("Planner", planner.get_planner_agent())
    builder.add_node("Researcher", researcher.get_researcher_agent())
    builder.add_node("Summarizer", summarizer.get_summarizer_agent())
    builder.add_node("Critic", critic.get_critic_agent())
    builder.add_node("Presenter", presenter.get_presenter_agent())
    
    # Core workflow
    builder.set_entry_point("Planner")
    builder.add_edge("Planner", "Researcher")
    builder.add_edge("Researcher", "Summarizer")
    builder.add_edge("Summarizer", "Critic")
    
    def critic_condition(state):
        # Hard stop after 2 cycles, or if "improve" not in output
        if state.get("improvement_count", 0) >= 2:
            return "Presenter"
        if "improve" in state.get("output", "").lower():
            return "Summarizer"
        return "Presenter"

    builder.add_conditional_edges("Critic", critic_condition)
    builder.set_finish_point("Presenter")
    
    return builder.compile()