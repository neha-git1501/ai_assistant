from app.rag.chunking import split_text
from app.rag.vector_store import create_vector_store
from app.rag.retriever import get_retriever

text="""
IMS registration can fail when the SIP REGISTER request does not receive a response within the configured timeout.
The issue may be related to network connectivity, timeout configuration, or SIP signalling problems.
"""
chunks=split_text(text)
print("chunks:")
for chunk in chunks:
    print(chunk)
vector_store=create_vector_store(chunks)
retriever=get_retriever(
    vector_store,
    top_k=3,
)
query="Why can IMS registration fail?"
documents=retriever.invoke(query)
print('\nRetrieved results:')
for doc in documents:
    print(doc.page_content)
