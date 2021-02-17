class QuizBrain:
    def __init__(self, q_list):
        self.num = 0
        self.list = q_list
        self.score = 0

    def generate_question(self):
        current = self.list[self.num]
        self.num += 1
        user = input(f'Q.{self.num} {current.text} ').title()
        self.check_answer(user, current.answer)

    def next_question(self):
        for _ in self.list:
            self.generate_question()
        else:
            return False

    def check_answer(self, user, correct):
        if user == correct:
            self.score += 1
            print(f"Correct, score = {self.score}/{self.num}.\n")
        else:
            print(f"Wrong, score = {self.score}/{self.num}.\n")