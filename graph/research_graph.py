from langgraph.graph import StateGraph, END

from state import ResearchState


from agents.manager import manager_agent
from agents.search_agent import search_agent
from agents.paper_agent import paper_agent
from agents.rag_agent import rag_agent
from agents.writer_agent import writer_agent
from agents.reviewer_agent import reviewer_agent
from agents.retriever_agent import retriever_agent


builder = StateGraph(ResearchState)


builder.add_node("manager", manager_agent)
builder.add_node("search", search_agent)
builder.add_node("paper", paper_agent)
builder.add_node("rag", rag_agent)
builder.add_node("writer", writer_agent)
builder.add_node("reviewer", reviewer_agent)
builder.add_node("retriever", retriever_agent)

builder.set_entry_point("manager")


builder.add_edge("manager", "search")
builder.add_edge("search", "paper")
builder.add_edge("paper", "rag")
builder.add_edge("rag", "retriever")
builder.add_edge("retriever", "writer")
builder.add_edge("writer", "reviewer")
builder.add_edge("reviewer", END)


graph = builder.compile()
