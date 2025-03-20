from dotenv import load_dotenv

load_dotenv()

from graph.chains.retrieval_grader import GradeDocuments, retrieval_grader
from ingestion import retriever
from pprint  import pprint
from graph.chains.generation import generation_chain

def test_retrival_grader_answer_yes()-> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    doc_txt = docs[0].page_content # take most relevent doc
    res: GradeDocuments = retrieval_grader.invoke(
        {"question": question, "document": doc_txt}
    )

    assert res.binary_score=='yes'

def test_tetrival_grader_answer_no()-> None:
    question = 'agent memory'
    docs = retriever.invoke(question)
    doc_txt = docs[0].page_content

    res: GradeDocuments = retrieval_grader.invoke(
        {"question": "how to make pizza", "document": doc_txt}
    )

    assert res.binary_score == "no"

def test_generation_chain() -> None:
    question = 'agent memory'
    docs = retriever.invoke(question)
    generation = generation_chain.invoke(
        {"context": docs, "question": question}
    )
    pprint(generation)
