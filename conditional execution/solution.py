# Solution for burgerorder
print("welcom to burger shop !")
size = input("what size burger do you want? M, N or L")
add_mushroom = input("do you want mushroom? Y or N")
extra_cheese = input("Do you want extra cheese ? Y or N")

bill = 0

if size == "M":
    bill += 5
elif size == "N":
    bill += 8
else:
    bill += 10
if add_mushroom == "Y":
    if size == "L":
        bill += 2
    else:
        bill += 1

if extra_cheese =="Y":
    bill += 1
print(f"your final bill is:{bill}")
