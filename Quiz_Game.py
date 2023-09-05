import random

python_quiz_questions = [
    {
        'question': 'What is Python?',
        'options': ['A reptile', 'A programming language', 'A type of snake'],
        'correct_answer': 'A programming language'
    },
    {
        'question': 'What is the main use of Python?',
        'options': ['Web development', 'Data analysis', 'All of the above'],
        'correct_answer': 'All of the above'
    },
    {
        'question': 'What is the result of 2 + 3 in Python?',
        'options': [],
        'correct_answer': '5'
    },
    {
        'question': 'Which of the following is not a Python data type?',
        'options': ['Integer', 'Float', 'Boolean', 'String', 'Character'],
        'correct_answer': 'Character'
    },
    {
        'question': 'What is the purpose of the `if` statement in Python?',
        'options': ['To define a function', 'To perform a loop', 'To make decisions', 'To import libraries'],
        'correct_answer': 'To make decisions'
    },
    {
        'question': 'What is the output of `print(3 * "Hello ")`?',
        'options': [],
        'correct_answer': 'Hello Hello Hello '
    },
    {
        'question': 'What is the result of `2 ** 3` in Python?',
        'options': [],
        'correct_answer': '8'
    },
    {
        'question': 'Which of the following is used to add comments in Python?',
        'options': ['#', '/*', '//', '*/'],
        'correct_answer': '#'
    },
    {
        'question': 'What is the correct way to define a Python function?',
        'options': ['function myFunction():', 'def myFunction():', 'func myFunction():', 'define myFunction():'],
        'correct_answer': 'def myFunction():'
    },
    {
        'question': 'Which Python module is used for regular expressions?',
        'options': ['regex', 're', 'regexpy', 'pyre'],
        'correct_answer': 're'
    },
    {
        'question': 'What does the `len()` function return for a string?',
        'options': ['The number of words', 'The number of characters', 'The number of lines', 'The number of vowels'],
        'correct_answer': 'The number of characters'
    },
    {
        'question': 'What is the purpose of the `elif` statement in Python?',
        'options': ['To define a function', 'To perform a loop', 'To make decisions', 'To check multiple conditions'],
        'correct_answer': 'To check multiple conditions'
    },
    {
        'question': 'Which of the following data structures is mutable in Python?',
        'options': ['Lists', 'Tuples', 'Strings', 'Dictionaries'],
        'correct_answer': 'Lists'
    },
    {
        'question': 'What is the output of `print("Python"[::-1])`?',
        'options': [],
        'correct_answer': 'nohtyP'
    },
    {
        'question': 'What does the `import` statement do in Python?',
        'options': ['Exports a module', 'Imports a module', 'Defines a function', 'Deletes a variable'],
        'correct_answer': 'Imports a module'
    },
    {
        'question': 'In Python, what is used to represent an empty block of code?',
        'options': ['pass', 'break', 'continue', 'None'],
        'correct_answer': 'pass'
    },
    {
        'question': 'Which of the following is a Python reserved word?',
        'options': ['variable', 'function', 'for', 'index'],
        'correct_answer': 'for'
    },
    {
        'question': 'What is the correct way to open a file in Python for reading?',
        'options': ['file.open("filename.txt", "r")', 'open("filename.txt")', 'open("filename.txt", "read")', 'file.read("filename.txt")'],
        'correct_answer': 'open("filename.txt")'
    },
    {
        'question': 'How do you create a set in Python?',
        'options': ['Using square brackets', 'Using curly braces', 'Using angle brackets', 'Using parentheses'],
        'correct_answer': 'Using curly braces'
    },
    {
        'question': 'What is the output of `bool(0)` in Python?',
        'options': [],
        'correct_answer': 'False'
    },
    {
        'question': 'Which of the following is a valid variable name in Python?',
        'options': ['2myVar', 'my-var', '_myVar', 'my Var'],
        'correct_answer': '_myVar'
    },
    {
        'question': 'What is the purpose of the `range()` function in Python?',
        'options': ['To create a list of numbers', 'To generate a random number', 'To iterate over a sequence of numbers', 'To calculate the factorial of a number'],
        'correct_answer': 'To iterate over a sequence of numbers'
    }
]

def display_welcome_message():
    print("Welcome to the Python Quiz Game!")
    print("Here are the rules:")
    print("1. Answer Python-related questions.")
    print("2. Earn points for correct answers.")
    print("3. Get feedback on each answer.")
    print("4. Try to score as high as possible!\n")

def present_quiz_questions():
    score = 0
    for question_data in python_quiz_questions:
        question = question_data['question']
        options = question_data['options']
        correct_answer = question_data['correct_answer']

        print(question)
        if len(options) > 0:
            for i, option in enumerate(options, start=1):
                print(f"{i}. {option}")
            user_answer = input("Enter the number of your answer: ")
            try:
                user_answer = int(user_answer)
                if 1 <= user_answer <= len(options):
                    user_answer = options[user_answer - 1]
                else:
                    raise ValueError
            except ValueError:
                user_answer = input("Invalid input. Please enter a valid option: ")
        else:
            user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}\n")

    return score

def main():
    while True:
        display_welcome_message()
        score = present_quiz_questions()
        print(f"Your final score is: {score}/{len(python_quiz_questions)}")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
