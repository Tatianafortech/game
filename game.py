# game.py

def run_quiz(answer):
    score = 0
    total_questions = 3

    print('Welcome to AskPython Quiz')
    user_ready = input('Are you ready to play the Quiz? (yes/no): ')

    if user_ready.lower() == 'yes':
        answer_1 = input('Question 1: What is your favorite programming language? ')
        if answer_1.lower() == 'python':
            score += 1
            print('Correct!')
        else:
            print('Wrong Answer :(')

        answer_2 = input('Question 2: Do you follow any author on AskPython? ')
        if answer_2.lower() == 'yes':
            score += 1
            print('Correct!')
        else:
            print('Wrong Answer :(')

        answer_3 = input('Question 3: What is the name of your favorite website for learning Python? ')
        if answer_3.lower() == 'askpython':
            score += 1
            print('Correct!')
        else:
            print('Wrong Answer :(')

    print(f'Thank you for playing this small quiz game. You attempted {score} questions correctly!')
    mark = (score / total_questions) * 100
    print(f'Marks obtained: {mark}')
    print('BYE!')

if __name__ == '__main__':
    run_quiz('python')  # You can replace this with user input if needed
