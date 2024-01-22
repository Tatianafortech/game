# game.py

def run_quiz(user_ready='yes', answer_1='python', answer_2='yes', answer_3='askpython'):
    score = 0
    total_questions = 3

    print('Welcome to AskPython Quiz')
    if user_ready.lower() == 'yes':
        if input('Question 1: What is your favorite programming language? ').lower() == answer_1:
            score += 1
            print('Correct!')
        else:
            print('Wrong Answer :(')

        if input('Question 2: Do you follow any author on AskPython? ').lower() == answer_2:
            score += 1
            print('Correct!')
        else:
            print('Wrong Answer :(')

        if input('Question 3: What is the name of your favorite website for learning Python? ').lower() == answer_3:
            score += 1
            print('Correct!')
        else:
            print('Wrong Answer :(')

    print(f'Thank you for playing this small quiz game. You attempted {score} questions correctly!')
    mark = (score / total_questions) * 100
    print(f'Marks obtained: {mark}')
    print('BYE!')

if __name__ == '__main__':
    run_quiz()
