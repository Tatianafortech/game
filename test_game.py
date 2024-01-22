# test_game.py

import unittest
from unittest.mock import patch
from game import run_quiz

class TestGame(unittest.TestCase):
    @patch('builtins.input', side_effect=['yes', 'python', 'yes', 'askpython'])
    def test_answer_is_python(self, mock_input):
        self.assertEqual(run_quiz(), None)

    @patch('builtins.input', side_effect=['no', 'python', 'yes', 'askpython'])
    def test_answer_is_not_python(self, mock_input):
        self.assertEqual(run_quiz(), None)

    @patch('builtins.input', side_effect=['no', 'python', 'yes', 'askpython'])
    def test_answer_is_not_python(self, mock_input):
        self.assertEqual(run_quiz_correct(), None)
        
if __name__ == '__main__':
    unittest.main()
