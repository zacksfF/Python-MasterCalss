import csv

csv_data = open("CSV tutorial/test.csv", 'w')

write = csv.writer(csv_data, delimiter=';')

header = ['Last name', 'First name', 'Age', 'Country']

data = ['zakaria', 'saif', '21', 'morocco']

write.writerow(header)

write.writerow(data)

csv_data.close()