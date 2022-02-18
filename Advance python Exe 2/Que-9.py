import csv
f1 = open('erps.csv', 'r')
print([tuple(line) for line in csv.reader(f1)][1:])
# print(data)

f1.close()
