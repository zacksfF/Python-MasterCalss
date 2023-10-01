string = 10

with open(youFile.txt) as f:
    for line in f:
        print(str(string) + " . "+ line)
        string += 10