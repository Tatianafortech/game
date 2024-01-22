def run_quiz():
    questions = [
        ('What is the capital of France?', 'paris'),
        ('Is the sun hot? (yes/no)', 'yes'),
        ('How many continents are there? (numeric)', '7')
    ]

    score = 0
    total_questions = len(questions)

    print('Welcome to the Quiz!')
    for question, correct_answer in questions:
        user_answer = input(question).lower()
        if user_answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(f'Wrong Answer. The correct answer is {correct_answer}.')

    print(f'Thank you for playing. You got {score} out of {total_questions} questions correct!')
    percentage = (score / total_questions) * 100
    print(f'Marks obtained: {percentage:.2f}%')
    print('BYE!')

if __name__ == '__main__':
    run_quiz()
