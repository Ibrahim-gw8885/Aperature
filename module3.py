import csv
from datetime import datetime
from datetime import date


with open('fridge2.0.csv') as fridge_csv:
  fridge_reader = csv.DictReader(fridge_csv, delimiter='@')
  month = [int(book['expmonth']) for book in fridge_reader]


with open('fridge2.0.csv') as fridge1_csv:
  fridge1_reader = csv.DictReader(fridge1_csv, delimiter='@')
  day = [int(book1['expday']) for book1 in fridge1_reader]

with open('fridge2.0.csv') as fridge1_csv:
  fridge1_reader2 = csv.DictReader(fridge1_csv, delimiter='@')
  products = [book2['food'] for book2 in fridge1_reader2]
             

current_time = date.today()


for num in range(len(day)):
    exp_date = date(2022, month[num], day[num])
    new = products[num]
    
    if exp_date <= current_time:

        print(new.title() + ": Its Expired")
    
    else:

        print(new.title() + ": Not Expired")



