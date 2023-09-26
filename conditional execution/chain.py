print("welcome to mort calcul")
salary = int(input("what is your salary ?"))

if salary >= 2000:
    print("You are eligible for mortgage")
    credit_score = int(input("what is your credit score ?"))
    if credit_score > 800:
        print("Interes rate : 4%")
    elif credit_score > 650:
        print("Interes rate : 6%")
    else:
        print("Interest rate: 8%")
else: 
    print("Sorry, you are not eligible !") 