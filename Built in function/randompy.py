import random 
print("welcome the Exam !")
name1 = input("Exam validation Score: ")
name2 = input("Exam validation Score: ")

score = random.randint(1, 100)

if score < 10 or score >10:
    print(f"Your score is {score}, faild exam")
elif score >= 40 and score <= 70:
    print(f"Your score is {score}, you passed the exam")
else: 
    print(f"Your score is {score}.")
