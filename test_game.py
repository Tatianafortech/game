import unittest
from unittest.mock import patch, call
from game import run_quiz, get_user_input

class TestGame(unittest.TestCase):
    @patch('builtins.input', side_effect=['paris', 'yes', '7'])
    @patch('builtins.print')
    def test_run_quiz_all_correct_answers(self, mock_print, mock_input):
        run_quiz()
        expected_calls = [
            call('Welcome to the Quiz!'),
            call('Correct!'),
            call('Correct!'),
            call('Correct!'),
            call('Thank you for playing. You got 3 out of 3 questions correct!'),
            call('Marks obtained: 100.00%'),
            call('BYE!')
        ]
        mock_print.assert_has_calls(expected_calls)
        print("Output for 'test_run_quiz_all_correct_answers':")
        # for call_args in mock_print.call_args_list:
            # print(call_args)

    @patch('builtins.input', side_effect=['london', 'no', '5'])
    @patch('builtins.print')
    def test_run_quiz_some_incorrect_answers(self, mock_print, mock_input):
        run_quiz()
        expected_calls = [
            call('Welcome to the Quiz!'),
            call("Wrong Answer. The correct answer is paris."),
            call("Wrong Answer. The correct answer is yes."),
            call("Wrong Answer. The correct answer is 7."),
            call('Thank you for playing. You got 0 out of 3 questions correct!'),
            call('Marks obtained: 0.00%'),
            call('BYE!')
        ]
        mock_print.assert_has_calls(expected_calls)
        print("Output for 'test_run_quiz_some_incorrect_answers':")
        # for call_args in mock_print.call_args_list:
        #     print(call_args)

    @patch('builtins.input', return_value='user_input')
    @patch('builtins.print')

    def test_get_user_input(self, mock_print, mock_input):
        result = get_user_input('Enter something: ')
        self.assertEqual(result, 'user_input')
        
        print("Output for 'test_get_user_input':")
        for call in mock_print.mock_calls:
            print(call)
    # def test_get_user_input(self, mock_print, mock_input):
    #     result = get_user_input('Enter something: ')
    #     self.assertEqual(result, 'user_input')
    #     # print("Output for 'test_get_user_input':")
    #     # for call_args in mock_print.call_args_list:
    #     #     print(call_args)

if __name__ == '__main__':
    unittest.main()
