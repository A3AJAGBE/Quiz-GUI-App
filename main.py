# Imports
from question import Question
from data import question_data
from brain import QuizBrain
from quiz_interface import QuizInterface

# Create Question Instance
question_info = []
for info in question_data:
    q = info['question']
    a = info['correct_answer']
    question_info.append(Question(q, a))

# Instances
quiz_brain = QuizBrain(question_info)
quiz_interface = QuizInterface(quiz_brain)

