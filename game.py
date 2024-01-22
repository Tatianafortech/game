# game.py

def run_quiz(user_ready='yes', answer_1='python', answer_2='yes', answer_3='askpython'):
    score = 0
    total_questions = 3

    print('Welcome to AskPython Quiz')
    if user_ready.lower() == 'yes':
        if ask_question('Question 1: What is your favorite programming language?', answer_1):
            score += 1

        if ask_question('Question 2: Do you follow any author on AskPython?', answer_2):
            score += 1

        if ask_question('Question 3: What is the name of your favorite website for learning Python?', answer_3):
            score += 1

    print(f'Thank you for playing this small quiz game. You attempted {score} questions correctly!')
    mark = (score / total_questions) * 100
    print(f'Marks obtained: {mark}')
    print('BYE!')

def ask_question(question, correct_answer):
    user_answer = input(question).lower()
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print('Wrong Answer :(')
        return False

def run_tests():
    # Run the quiz with correct answers for testing purposes
    run_quiz_correct(answer_1='python', answer_2='yes', answer_3='askpython')

if __name__ == '__main__':
    run_quiz()
    run_tests()
