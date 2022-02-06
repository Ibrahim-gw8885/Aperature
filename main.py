from asyncore import write
import tkinter as tk
import datetime
import csv
from datetime import datetime
from datetime import date

from pandas.core.base import DataError


shawzub = 1


class apt:

    #fridge = 'https://github.com/Ibrahim-gw8885/Aperature/blob/main/fridge.csv' - trying to use online git file
    fridge = 'fridge.csv'

    def __init__ (self):
        pass
    
    def returnDaysRemaining():
        pass

    def readAllItemsFromCsv():
        with open(apt.fridge, mode = 'r') as file:
            csvReader = csv.reader(file)
            for lines in csvReader:
                print(lines)
    
    def readAllFoods():
        with open(apt.fridge, mode = 'r') as file:
            csvReader = csv.reader(file)
            for lines in csvReader:
                print(lines[0])
    
    def readAllExp_dates():
        with open(apt.fridge, mode = 'r') as file:
            csvReader = csv.reader(file)
            for lines in csvReader:
                print(lines[1])

    def writeItemToCsv(foodName,exp_date):
        foodName = str(foodName)
        rowWrite = [foodName,exp_date]

        with open(apt.fridge, mode = 'a',newline='') as file:
            csvWriter = csv.writer(file)
            csvWriter.writerow(rowWrite)

    def returnFoodAndExp(foodName):
        #takes in the Name of the food and finds where it is in the csv file
        foodName = str(foodName) # makes sure the food name is a str
        index = 0 #is there a better way to find the index of the foodName?

        with open(apt.fridge, mode = 'r') as file:
                    csvReader = csv.reader(file)
                    for lines in csvReader:
                        index= index + 1
                        if lines[0] == foodName:
                            print('food found at index:', str(index))
                            return index
                        else:
                            print(lines.count) # debugging code


    class gui:
        def __init__(self):
            pass
        
        def inputWidget():
            inputWidgetCol = tk.Frame(root)



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



