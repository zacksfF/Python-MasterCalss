def capallwords(x):
    return x.title()

countries = ["morocco", "usa", "italie"]
result = map(capallwords, countries)

print(list(result))