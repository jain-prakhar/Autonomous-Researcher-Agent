import os

from graph.research_graph import graph
from utils.pdf_generator import save_pdf

os.makedirs("outputs", exist_ok=True)

result = graph.invoke(
    {
        "query": "Future of multimodal large language models in enterprise applications"
    }
)

print("\n========== RETRIEVED CONTEXT ==========\n")
print(result["retrieved_context"][:1500])
print("\n========== REVIEW COMMENTS ==========\n")
print(result["review_comments"])

save_pdf(
    result["final_report"],
    "outputs/report.pdf"
)
