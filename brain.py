import html


class QuizBrain:
    def __init__(self, q_list):
        self.num = 0
        self.list = q_list
        self.score = 0
        self.current = None

    def generate_question(self):
        self.current = self.list[self.num]
        self.num += 1
        question = html.unescape(self.current.text)
        return f'Q.{self.num}: {question} '

    def next_question(self):
        return self.num < len(self.list)

    def check_answer(self, user):
        correct = self.current.answer
        if user == correct:
            self.score += 1
            return True
        else:
            return False
