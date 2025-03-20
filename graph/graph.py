# create graph
from dotenv import load_dotenv

from langgraph.graph import END, StateGraph, START
from graph.consts import RETRIEVE, GRAGE_DOCUMENTS, GENERATE, WEBSEARCH

# if you don't want to write below 4 import uncomment the code in __init__.py of nodes package
from graph.nodes.generate import generate 
from graph.nodes.grade_documents import  grade_documents
from graph.nodes.retrieve import retrieve
from graph.nodes.web_search import web_search

from graph.state import State
load_dotenv()


def decide_to_generate(state: State):
    print("---ASSESS GRADED DOCUMENTS---")
    if state['web_search']:
        print("---DECISION: NOT ALL DOCUMENTS ARE NOT RELEVENT TO QUESTION.")
        return 'do web search'
    else:
        print('---DECISION: GENERATE---')
        return 'generate'
    
workflow = StateGraph(State)

workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRAGE_DOCUMENTS, grade_documents)
workflow.add_node(GENERATE, generate)
workflow.add_node(WEBSEARCH, web_search)

workflow.add_edge(START, RETRIEVE)
workflow.add_edge(RETRIEVE, GRAGE_DOCUMENTS)
workflow.add_conditional_edges(
    GRAGE_DOCUMENTS,
    decide_to_generate,
    {
        'do web search': WEBSEARCH,
        'generate': GENERATE

    }
)

workflow.add_edge(WEBSEARCH, GENERATE)
workflow.add_edge(GENERATE, END)

app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path='graph.png')
    



