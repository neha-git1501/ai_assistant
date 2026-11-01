from app.rag.chunking import split_text
text="""
IMS registration can fail when SIP REGISTER request times out.
Network issues can also cause registration failure.
"""
chunks = split_text(text)
print("="*60)
print("Number of Chunks:", len(chunks))
print("="*60)
for i, chunk in enumerate(chunks):
    print(f'\nChunk {i+1}')
    print(chunk)

