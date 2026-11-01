from langchain_community.vectorstores import FAISS
def get_retriever(
        vector_store: FAISS,
        top_k: int= 5,
):
    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": top_k
        }
    )