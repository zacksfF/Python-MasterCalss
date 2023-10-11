thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

numlist = [100, 50, 65, 82, 23]
numlist.sort()
print(numlist)

thislist.sort(reverse = True)
print(thislist)

##### Customize Sort Function
def myfunc(n):
  return abs(n - 50)

numlist.sort(key = myfunc)
print(numlist)