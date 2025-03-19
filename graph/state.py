from typing import List, TypedDict

class State(TypedDict):
    """
    Represents the state of our graph

    Attributes:
        question: user question
        generation: LLM generation
        web_search: whether to add search
        documents: context (list of document returned from vector store)
    """

    question:str
    generation: str
    web_search: bool
    documents: List[str]