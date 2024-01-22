import unittest
from unittest.mock import patch
from game import run_quiz

class TestGame(unittest.TestCase):
    @patch('builtins.input', side_effect=['python', 'yes', 'askpython'])
    def test_run_quiz_correct_answers(self, mock_input):
        with patch('builtins.print') as mock_print:
            run_quiz()
            mock_print.assert_called_with(
                'Welcome to AskPython Quiz',
                'Correct!',
                'Correct!',
                'Correct!',
                'Thank you for playing. You got 3 out of 3 questions correct!',
                'Marks obtained: 100.00%',
                'BYE!'
            )

    @patch('builtins.input', side_effect=['java', 'no', 'w3schools'])
    def test_run_quiz_incorrect_answers(self, mock_input):
        with patch('builtins.print') as mock_print:
            run_quiz()
            mock_print.assert_called_with(
                'Welcome to AskPython Quiz',
                'Wrong Answer :(',
                'Wrong Answer :(',
                'Wrong Answer :(',
                'Thank you for playing. You got 0 out of 3 questions correct!',
                'Marks obtained: 0.00%',
                'BYE!'
            )

if __name__ == '__main__':
    unittest.main()
