# Solution to BMI calculator
height = float(input("Enter your Height in m: "))
weight = float(input("Enter your weigh in KG: "))

bmi = round(weight / height ** 2,2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underwight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you weight is normal.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overwight.")
else:
    print(f"Your bmi is {bmi}, you are obese.")
