from app.services.query_service import ask_question
question="Why did the issue described in the uploaded document occur?"
answer=ask_question(question)
print("="*60)
print("QUESTION:")
print(question)
print("="*60)
print("ANSWER:")
print(answer)
print("="*60)
