# Not sure why first file got deleted when attempting to create a second file. Therefore will be redoing the code here.
# Code and commits will be identical to original(deleted) file, as I can still view it but can no longer retrieve it.

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer
    
class AdditionQuestion(Question):
    def __init(self, a, b):
        super().__init__(f"{a} + {b}", a + b)

class SubtractionQuestion(Question):
    def __init__(self, a, b):
        if a < b:
            a, b = b, a
        super().__init__(f"{a} - {b}", a - b)