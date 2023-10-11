mylist = [3,4,5,7,"banana", "fruit", "sigg"]
#print(mylist)

#first_list = mylist[0]
#print(first_list)

#sub_list = mylist[1:4]
#print(sub_list)

#modifiying lists 

#mylist.append("zack")
##print(mylist)


mylist = [3,4,5,7,"banana", "fruit", "sigg"]
mylist.insert(0, "dee")
print(mylist)

print(len(mylist))

thislist = list(("apple", "banana", "cherry"))
print(thislist)


#duplicate 
list = ["apple", "huice", "lemon", "apple"]
print(list)

#Types
list10 = ["fsr", 14, False, "amam"]
print(type(list10))
#<class 'list'>

#indexing
print(mylist[0:4])

thislist = ["apple", "banana", "cherry"]
print(thislist[0:2:-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-5:4])

if "cherry" in thislist:
    print("yes this word in list")
else:
    print("false is not in thislist")

#Change List Items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#thislist[2] = "backk"
thislist[1:3] = ["watermelon"]
print(thislist)
print(thislist[-1])

#Insert list ot items 
thislist.insert(2, "watermelon")
print(thislist)

#add items
thislist.append("kiwiw")
print(thislist)

#Extend List
trop = ["mango", "pineapple", "papaya"]
thislist.extend(trop)
print(thislist)

thislist.remove("mango")
print(thislist)

#Remove Specified Index
list = ["apple", "banana", "cherry"]
list.pop(1)
print(list)

list = ["apple", "cherry"]
del list

#clear
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#loop list
hislist = ["apple", "main", "qua", "banana", "cherry"]
for x in hislist:
    print(x)

for i in range (len(hislist)):
    print(hislist[i])