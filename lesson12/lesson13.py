import pandas as pd
#products=['apples','grapes','oranges','bananas']
#sales=[150,200,180,90]
#sales_series=pd.Series(sales,index=products)
#print(sales_series)
#total_sales













#data={'Name':['Klea','Emily','Lay'],
    #  'Age':[17,24,39],
     # 'City':['Prishtine','Paris','New York']
      #}
#df=pd.DataFrame(data)
#print(df)

data=[
    ['Name','Age','City'],
    ['Klea',17,'Prishtine'],
    ['Emily',24,'Paris'],
    ['Lay',39,'New York']
]
import csv
with open ('example.csv','w',newline='') as file:
    writer= csv.writer(file)
    writer.writerows(data)

    print("Data written to example.csv")
with open ('example.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)









