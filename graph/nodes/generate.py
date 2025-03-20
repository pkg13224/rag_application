from typing import Any, Dict
from graph.chains.generation import generation_chain
from graph.state import State

def generate(state: State)->Dict[str, Any]:
    print("---GENERATE---")
    question = state['question']
    documents = state['documents']

    generation = generation_chain.invoke(
        {'context': documents, 'question': question}
    )
    return {'generation': generation}