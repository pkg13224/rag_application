from typing import Any, Dict

from langchain.schema import Document

from langchain_community.tools.tavily_search import TavilySearchResults

from graph.state import State

from dotenv import load_dotenv

load_dotenv()

web_search_tool = TavilySearchResults(max_resutls = 3)

def web_search(state: State)-> Dict[str, Any]:
    print("---WEB SEARCH---")
    question  = state["question"]
    documents = state["documents"]

    tavily_results = web_search_tool.invoke({"query": question})
    joined_tavliy_result = "\n".join(
        [tavily_result["content"] for tavily_result in tavily_results]
    )

    web_results = Document(page_content=joined_tavliy_result)
    if documents is None:
        documents=[web_results]
    else:
        documents.append(web_results)

    return {"documents": documents}

if __name__=='__main__':
    web_search(state = {"question": "agent memory", "documents": None})