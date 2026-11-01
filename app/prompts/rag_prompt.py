from langchain_core.prompts import ChatPromptTemplate

rag_prompt=ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an enterprise engineering assistant.
            Answer the user's question using only the provided context.
            Do not invent information.
            If the context does not contain enough information to answer the question, 
            say that the information is not available in the provided knowledge base.
            
            Context:
            {context}
            """,

        ),
        (
            "human",
            "{question}",
        ),
    ]
)