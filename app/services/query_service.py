from app.rag.vector_store import load_vector_store
from app.rag.retriever import get_retriever
from app.rag.rag_chain import build_rag_chain

def ask_question(question: str)->str:
    vector_store = load_vector_store()
    retriever = get_retriever(vector_store)
    documents = retriever.invoke(question)
    sources=[]
    for document in documents:
        metadata=document.metadata
        source={
            "source":metadata.get(
                "source",
                "Unknown",
            ),
            "source_type":metadata.get(
                "source_type",
                "Unknown",
            ),
        }
        if source not in sources:
            sources.append(source)
    context="\n\n".join(
        [
            doc.page_content
            for doc in documents
        ]
    )
    chain = build_rag_chain()
    answer = chain.invoke(
        {
            "context":context,
            "question":question,
        }
    )
    return {
        "answer":str(answer),
        "sources":sources,
    }

