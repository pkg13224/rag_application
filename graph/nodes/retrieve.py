from typing import Any, Dict

from graph.state import State

from ingestion import retriever

def retrieve(state: State)-> Dict[str, Any]:
    print("---RETRIEVE---")
    question = state['question']
    documents = retriever.invoke(question)
    return {"documents": documents}