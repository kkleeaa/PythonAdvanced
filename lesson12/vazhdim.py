import csv

data= [
    {'Name':'Klea','Age':17,'City':'Prishtine'},
    {'Name':'Blin','Age':17,'City':'Prishtine'},
    {'Name':'Albina','Age':39,'City':'Prisshtine'}
]
header=['Name','Age','City']
with open('people.csv','w',newline='') as file:
    writer =csv.DictWriter(file,fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
print('data written to people.csv')
with (open ('people.csv','r') as file):
    reader=csv.DictReader(file)
    for row in reader:
        print(dict(row))



