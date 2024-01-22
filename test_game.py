# test_game.py

import unittest
from unittest.mock import patch
from game import run_quiz, ask_question

class TestGame(unittest.TestCase):
    @patch('builtins.input', side_effect=['yes', 'python', 'yes', 'askpython'])
    def test_run_quiz_correct_answers(self, mock_input):
        # Test the run_quiz function with correct answers
        with patch('builtins.print') as mock_print:
            run_quiz()
            mock_print.assert_called_with(
                "Welcome to AskPython Quiz",
                "Correct!",
                "Correct!",
                "Correct!",
                "Thank you for playing this small quiz game. You attempted 3 questions correctly!",
                "Marks obtained: 100.0",
                "BYE!"
            )

    @patch('builtins.input', side_effect=['no', 'java', 'no', 'w3schools'])
    def test_run_quiz_incorrect_answers(self, mock_input):
        # Test the run_quiz function with incorrect answers
        with patch('builtins.print') as mock_print:
            run_quiz()
            mock_print.assert_called_with(
                "Welcome to AskPython Quiz",
                "Wrong Answer :(",
                "Wrong Answer :(",
                "Wrong Answer :(",
                "Thank you for playing this small quiz game. You attempted 0 questions correctly!",
                "Marks obtained: 0.0",
                "BYE!"
            )

    def test_ask_question_correct_answer(self):
        # Test the ask_question function with correct answer
        with patch('builtins.input', return_value='python'):
            with patch('builtins.print') as mock_print:
                result = ask_question('What is your favorite programming language?', 'python')
                self.assertTrue(result)
                mock_print.assert_called_with('Correct!')

    def test_ask_question_incorrect_answer(self):
        # Test the ask_question function with incorrect answer
        with patch('builtins.input', return_value='java'):
            with patch('builtins.print') as mock_print:
                result = ask_question('What is your favorite programming language?', 'python')
                self.assertFalse(result)
                mock_print.assert_called_with('Wrong Answer :(')

if __name__ == '__main__':
    unittest.main()
