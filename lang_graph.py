from langgraph.graph import StateGraph, END
from agents.research_agent import research_node
from agents.answer_drafter_agent import draft_answer_node


def build_graph():
    builder = StateGraph(str)
    builder.add_node("ResearchAgent", research_node)
    builder.add_node("AnswerDrafterAgent", draft_answer_node)

    builder.set_entry_point("ResearchAgent")
    builder.add_edge("ResearchAgent", "AnswerDrafterAgent")
    builder.add_edge("AnswerDrafterAgent", END)

    return builder.compile()
