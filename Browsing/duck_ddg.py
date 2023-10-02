# pip install duckduckgo-search
from duckduckgo_search import DDGS
import csv 


with DDGS() as ddgs:
    results = [r for r in ddgs.text("Python programming", max_results=5)]
    results2 = [r for r in ddgs.text("machine learning with python", max_results=5)]
    results3 = [r for r in ddgs.text("Deep learning with python", max_results=5)]
    results4 = [r for r in ddgs.text("python for beginners", max_results=5)]
    print(results, results2, results3,results4 )

# To CSV
csv_file = open('search_results.csv', 'w')
writer = csv.writer(csv_file, delimiter =';')
keywords = 'CSV Rs'
for x in range(len(results)):
    row = [results[x]["title"],results[x]["body"],results[x]["href"]]
    writer.writerow(row)

csv_file.close()
