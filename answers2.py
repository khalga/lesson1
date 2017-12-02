question = input().lower()
answers =  {'hi':'hi there!', 'how are you?':'fine, and you?', 'bye':'see you'}
def get_answer(question, answers):
	return answers.get(question)
print(get_answer(question, answers))