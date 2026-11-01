from langchain_core.output_parsers import StrOutputParser
from app.llm.ollama_service import llm
from app.prompts.rag_prompt  import rag_prompt
def build_rag_chain():
    return(rag_prompt|llm|StrOutputParser())