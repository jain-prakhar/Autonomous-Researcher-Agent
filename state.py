from typing import TypedDict, List, Dict, Any


class ResearchState(TypedDict):
    query: str
    tasks: List[str]
    search_results: List[Dict[str, Any]]
    paper_results: List[Dict[str, Any]]
    draft_report: str
    final_report: str
    review_comments: str
    retrieved_context: str
    retrieved_sources: list
