from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    q_text = item["text"]
    q_answer = item["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("\nYou have completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")