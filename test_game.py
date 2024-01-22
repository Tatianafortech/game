# test_game.py

import unittest
from game import run_quiz

class TestGame(unittest.TestCase):
    def test_answer_is_python(self):
        self.assertEqual(run_quiz('python'), 1)

    def test_answer_is_not_python(self):
        self.assertEqual(run_quiz('no'), 0)

if __name__ == '__main__':
    unittest.main()
