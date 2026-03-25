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
          if a < b:
               a, b = b, a
          super().__init__(f"{a} - {b}", a - b)

class MultiplicationQuestion(Question):
     def __init__(self, a, b):
          super().__init__(f"{a} * {b}", a * b)

class DivisionQuestion(Question):
     def __init__(self, answer, divisor):
          # ensures no decimal answers
          dividend = answer * divisor
          super().__init__(f"{dividend} / {divisor}", answer)