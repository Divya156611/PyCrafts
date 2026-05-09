print("***************************************************\n Welcome to My Quiz Game \n\n *************************************************** ")
question_bank=[
     {
        "question":"1.What does OOP stand for?",
        "options":["A) Object Oriented Programming","B) Object Ordered Programming","C) Organized Object Process","D) Object Operating Program"],
        "answer":"A"
     },
     {
        "question":"2.Which concept allows one class to acquire properties of another class?",
        "options":["A) Polymorphism","B) Abstraction","C) Inheritance","D) Encapsulation"],
        "answer":"C"
     },
     {
        "question":"3.What is the process of hiding internal details and showing only essential features called?",
        "options":["A) Polymorphism","B) Abstraction","C) Inheritance","D) Encapsulation"],
        "answer":"B"
     },
     {
        "question":"4.Which principle of OOP allows objects to take on many forms?",
        "options":["A) Polymorphism","B) Abstraction","C) Inheritance","D) Encapsulation"],
        "answer":"A"
     },
     {
        "question":"5.What is the concept of bundling data and methods that operate on that data within a single unit called?",
        "options":["A) Polymorphism","B) Abstraction","C) Inheritance","D) Encapsulation"],
        "answer":"D"
     }
]
score=0
for ques in question_bank:
    print(ques["question"])
    for option in ques["options"]:
      print(f"{option}")
    answer=input("Enter your answer (A, B, C, D): ").upper()
    if answer == ques["answer"]:
         print(f"Correct Answer \nYour correct answer is option {answer}")
         score += 1
    else:
         print(f"Wrong Answer \nThe correct answer is {ques['answer']}")
    print(f"Your score is {score}/{len(question_bank)}")

print(f"Your final score is {score/len(question_bank)*100:.2f}%")