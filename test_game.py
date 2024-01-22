import unittest
from unittest.mock import patch
from game import run_quiz

class TestGame(unittest.TestCase):
    @patch('builtins.input', side_effect=['paris', 'yes', '7'])
    @patch('builtins.print')
    def test_run_quiz_all_correct_answers(self, mock_print, mock_input):
        run_quiz()
        expected_calls = [
            'Welcome to the Quiz!',
            'Correct!', 'Correct!', 'Correct!',
            'Thank you for playing. You got 3 out of 3 questions correct!',
            'Marks obtained: 100.00%',
            'BYE!'
        ]
        mock_print.assert_has_calls([call(msg) for msg in expected_calls])

    @patch('builtins.input', side_effect=['london', 'no', '5'])
    @patch('builtins.print')
    def test_run_quiz_some_incorrect_answers(self, mock_print, mock_input):
        run_quiz()
        expected_calls = [
            'Welcome to the Quiz!',
            "Wrong Answer. The correct answer is paris.",
            "Wrong Answer. The correct answer is yes.",
            "Wrong Answer. The correct answer is 7.",
            'Thank you for playing. You got 0 out of 3 questions correct!',
            'Marks obtained: 0.00%',
            'BYE!'
        ]
        mock_print.assert_has_calls([call(msg) for msg in expected_calls])

if __name__ == '__main__':
    unittest.main()
