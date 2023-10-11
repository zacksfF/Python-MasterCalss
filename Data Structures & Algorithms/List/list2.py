#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [expression for item in iterable if ocndition == True]
