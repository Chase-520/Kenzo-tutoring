import threading
import time

# Creating a lock for safe concurrent printing
print_lock = threading.Lock()


# Function to print the question and answer choices
def ask_question(question, choices, correct_answer):
    with print_lock:
        print("\n" + question)
        for i, choice in enumerate(choices, 1):
            print(f"{i}) {choice}")
        answer = input("Your answer: ")

        if answer == correct_answer:
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is {correct_answer}\n")
        time.sleep(1)  # Simulating delay between questions


# Defining quiz questions
questions = [
    ("What does the following code output?\n"
     "a = 5\nb = 10\nprint(a < b)",
     ["True", "False", "5", "Error"], "1"),

    ("What operator is used to check if two values are equal?",
     ["=", "==", "<", "!="], "2"),

    ("What is the output of this code?\nx = 'Python'\ny = 'python'\nprint(x == y)",
     ["True", "False", "python", "Error"], "2"),

    ("What will the following code print?\nif 7 >= 5:\n    print('Yes')\nelse:\n    print('No')",
     ["Yes", "No", "Error", "None of the above"], "1"),

    ("What is the result of this expression?\nresult = (10 > 5) and (5 < 3)\nprint(result)",
     ["True", "False", "Error", "None"], "2"),

    ("Which keyword is used to run code when all other conditions in an if-else chain are False?",
     ["elif", "if", "else", "for"], "3"),

    ("What is the output of this code?\na = (4 == 4) or (3 > 5)\nprint(a)",
     ["True", "False", "Error", "None"], "1")
]

# Creating threads for each question
threads = []
for i, (question, choices, correct_answer) in enumerate(questions):
    thread = threading.Thread(target=ask_question, args=(question, choices, correct_answer))
    threads.append(thread)

# Starting all threads
for thread in threads:
    thread.start()

# Waiting for all threads to finish
for thread in threads:
    thread.join()

print("Good job!")
