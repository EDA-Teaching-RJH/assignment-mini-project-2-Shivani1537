class Question:
    def __init__(self, text, answer):
         self.text = text
         self.answer = answer

    def check_answer(self, user_answer):
         return user_answer == self.answer

class AdditionQuestion(Question):
     def __init__(self, a, b):
          super().__init__(f"{a} + {b}", a + b)

class SubtractionQuestion(Question):
     def __init__(self, a, b):
          super().__init__(f"{a} - {b}", a - b)

class MultiplicationQuestion(Question):
     def __init__(self, a, b):
          super().__init__(f"{a} * {b}", a * b)