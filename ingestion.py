from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import os

load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')

urls = [
    'https://arxiv.org/list/cs.AI/recent',
    'https://lilianweng.github.io/posts/2023-06-23-agent/',
]

docs = [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 250, chunk_overlap = 50)
doc_splits = text_splitter.split_documents(docs_list)

# Save the document embeddings to this project root dir.
# vectorstore = Chroma.from_documents(
#     documents= doc_splits,
#     collection_name='rag-chroma',
#     embedding=OpenAIEmbeddings(),
#     persist_directory='./.chroma',
# )

retriever = Chroma(
    collection_name='rag-chroma',
    persist_directory='./.chroma',
    embedding_function= OpenAIEmbeddings()
).as_retriever()

