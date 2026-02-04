# Multiple Choice Quix in Python
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions_prompts = [
    "What is capital of Indonesia?\n (a) Kuala Lumpur\n (b) Jakarta\n (c) Manila\n\n",
    "Which continent does Romania lie in?\n (a) Asia\n (b) Europe\n (c) South America\n\n",
    "What is capital of Isle of Man?\n (a) Dublin\n (b) Bern\n (c) Douglas\n\n"
]

questions = [
    Question(questions_prompts[0], "b"),
    Question(questions_prompts[1], "b"),
    Question(questions_prompts[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)[0]
        if answer == question.answer:
            score += 1
    print(f"You got {score} / {len(questions)} correct")


run_test(questions)

