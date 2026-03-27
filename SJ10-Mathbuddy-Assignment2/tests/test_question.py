import unittest

from models.question import Question

class TestQuestion(unittest.TestCase):
    
    def test_correct_answer(self):
        q = Question("2 + 2", 4)
        self.assertTrue(q.check_answer(4))

    def test_wrong_answer(self):
        q = Question("2 + 2", 4)
        self.assertFalse(q.check_answer(5))

    def test_negative_answer(self):
        q = Question("5 - 10", -5)
        self.assertTrue(q.check_answer(-5))