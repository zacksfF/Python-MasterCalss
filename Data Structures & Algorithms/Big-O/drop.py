#O(2n)
def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
print_items(10)

# O*O*O(n)
def print_items(n):
    for i in range(n):
        for j in range(n):
            for f in range(n):
                print(i, j, f)
print_items(10)


