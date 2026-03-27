import unittest

from models.question import Question

class TestQuestion(unittest.TestCase):
    
    def test_correct_answer(self):
        q = Question("2 + 2", 4)
        self.assertTrue(q.check_answer(4))