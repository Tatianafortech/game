def run_quiz():
    score = 0
    questions = [
        ('What is your favorite programming language?', 'python'),
        ('Do you follow any author on AskPython?', 'yes'),
        ('What is the name of your favorite website for learning Python?', 'askpython')
    ]

    print('Welcome to AskPython Quiz')
    for question, correct_answer in questions:
        if input(question).lower() == correct_answer:
            print('Correct!')
            score += 1
        else:
            print('Wrong Answer :(')

    total_questions = len(questions)
    print(f'Thank you for playing. You got {score} out of {total_questions} questions correct!')
    percentage = (score / total_questions) * 100
    print(f'Marks obtained: {percentage:.2f}%')
    print('BYE!')

if __name__ == '__main__':
    run_quiz()
