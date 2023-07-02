import sys
sys.path.append("../classes")

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizUI

questions = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    questions.append(new_question)

quiz = QuizBrain(questions)
quiz_ui = QuizUI(quiz)
