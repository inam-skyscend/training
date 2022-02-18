# Create a CSV from the following list of dictionary.
# [
# {‘name':'Infosys', ‘location':'Pune','strength':40,000.0},
# {‘name':'TCS', ‘location':'Gandhinagar','strength':80,000.0},
# {‘name':'Wipro', ‘location':'Banguluru','strength':65,000.0},
# {‘name':'Accenture', ‘location':'Gurugram','strength':45,000.0},
# {‘name':'Capegemini', ‘location':'Mumbai','strength':32,000.0},
# ]

import csv

l1=[{'name':'Infosys', 'location':'Pune','strength':40000.0},
{'name':'TCS', 'location':'Gandhinagar','strength':80000.0},
{'name':'Wipro', 'location':'Banguluru','strength':65000.0},
{'name':'Accenture', 'location':'Gurugram','strength':45000.0},
{'name':'Capegemini', 'location':'Mumbai','strength':32000.0},
]
keys = l1[0].keys()
print(keys)
f=open('company_data.csv','w')
writer=csv.DictWriter(f,keys)
writer.writerows(l1)
f.close()
