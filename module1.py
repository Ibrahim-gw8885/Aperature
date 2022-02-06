from datetime import datetime
from datetime import date

big_list = {"products": ["milk", "eggs", "cheese", "meat"], "experation month": [2, 6, 7, 2], "experation day": [3, 3, 28, 6]}

products = []
day = []
month = []
datemonth = []

day.append(big_list["experation day"])
month.append(big_list["experation month"])
products.append(big_list["products"])

day1 = []
month1 = []
products1 = []

for items in day:
    for n in items:
        day1.append(n)
for i in month:
  for m in i:
    month1.append(m)
for k in products:
   for j in k:
       products1.append(j)

               

current_time = date.today()


for num in range(len(day1)):
    exp_date = date(2022, month1[num], day1[num])
    new = products1[num]
    
    if exp_date == current_time:

        print(new.title() + ": Its Expired")
    
    else:

        print(new.title() + ": Not Expired")



