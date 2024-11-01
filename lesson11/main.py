file_path="example.txt"
file=open(file_path,"r")
content=file.read()
print(content)
file.close()

import datetime
current_time=datetime.datetime.now()
print(current_time)
print("year", current_time.year)

#find the date after 100 days
specific_time=current_time()+datetime.timedelta(days=100)
print(specific_time)
