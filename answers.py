question = input()
answers = {'hi':'hi there!', 'how are you':'fine, and you?', 'bye':'see you'}
def  get_answer(question, answers):
	return answers[question.lower()]
a = get_answer(question, answers)
print(a.lower())