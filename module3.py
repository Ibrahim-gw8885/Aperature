from datetime import datetime
from datetime import date
import csv



#pulling the information from the fridge file
with open('fridge2.0.csv') as fridge_csv:
  
   fridge_reader = csv.DictReader(fridge_csv, delimiter=',')
  #putting the information read in fridge for a list of months
   month = [int(book['expmonth']) for book in fridge_reader]


#pulling the information from the fridge file
with open('fridge2.0.csv') as fridge1_csv:
  fridge1_reader = csv.DictReader(fridge1_csv, delimiter=',')


  #putting the information read in fridge for a list of day
  day = [int(book1['expday']) for book1 in fridge1_reader]


#pulling the information from the fridge file
with open('fridge2.0.csv') as fridge1_csv:
  fridge1_reader2 = csv.DictReader(fridge1_csv, delimiter=',')


  #putting the information read in fridge for a list of products
  products = [book2['food'] for book2 in fridge1_reader2]
             
#getting the date for today which will be compared to the expiration
current_time = date.today()

#A loop fuction which will take each value from the list to seprate them into day and month 

for num in range(len(day)):
    #this will format the information we have to make a easier to compare to the current date
    exp_date = date(2022, month[num], day[num])
    new = products[num]
    
    #this will out put the products that have expired because the products that havent exipred will not show up
    if exp_date <= current_time:

        print(new.title() + ": Its Expired")
    
 



