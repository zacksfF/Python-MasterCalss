print("welcome to mort calcul")
salary = int(input("what is your salary ?"))

if salary >= 2000:
    print("You are eligible for mortgage")
    credit_score = int(input("what is your credit score ?"))
    if credit_score > 800:
        print("Interes rate : 4%")
    else:
        print("Interest rate: 6%")
else: 
    print("Sorry, you are not eligible !") 