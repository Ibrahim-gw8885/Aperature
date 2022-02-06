from asyncore import write
from ctypes import alignment
import tkinter as tk
import datetime
import csv
from datetime import datetime
from datetime import date
from turtle import left
from click import command

from pandas.core.base import DataError


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

    def writeItemToCsv(foodName,month,day,year):
        foodName = str(foodName)
        rowWrite = [foodName,month,day,year]

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


    def determineExpired():
        
        #pulling the information from the fridge file
        with open('fridge.csv') as fridge0_csv:
  
            fridge0_reader = csv.DictReader(fridge0_csv, delimiter=',')
            
            #putting the information read in fridge for a list of years
            year = [int(book0['expyear']) for book0 in fridge0_reader]

        
        
        #pulling the information from the fridge file
        with open('fridge.csv') as fridge_csv:
  
            fridge_reader = csv.DictReader(fridge_csv, delimiter=',')
            
            #putting the information read in fridge for a list of months
            month = [int(book['expmonth']) for book in fridge_reader]


        #pulling the information from the fridge file
        with open('fridge.csv') as fridge1_csv:
            fridge1_reader = csv.DictReader(fridge1_csv, delimiter=',')


            #putting the information read in fridge for a list of day
            day = [int(book1['expday']) for book1 in fridge1_reader]


        #pulling the information from the fridge file
        with open('fridge.csv') as fridge1_csv:
            fridge1_reader2 = csv.DictReader(fridge1_csv, delimiter=',')


            #putting the information read in fridge for a list of products
            products = [book2['food'] for book2 in fridge1_reader2]
             
        #getting the date for today which will be compared to the expiration
        current_time = date.today()

        #A loop fuction which will take each value from the list to seprate them into day and month 
        for num in range(len(day)):
            
            #this will format the information we have to make a easier to compare to the current date
            exp_date = date(year[num], month[num], day[num])
            new = products[num]
    
        #this will out put the products that have expired because the products that havent exipred will not show up
        if exp_date <= current_time:

            print(new.title() + ": Its Expired")
        else:
            print(new.title() + ": not Expired")
    
    

        

    
 



    class gui:
        def __init__(self):
            self.root = tk.Tk()

            self.entryFrameW()

            self.root.mainloop() #loops the app
        
        def entryFrameW(self):
            self.entryFrame = tk.Frame(self.root,height=500,width=300)
            self.entryFrame.pack(side = tk.LEFT)

            #each text box widget has a lable and a entry box
            #Food entry widget
            self.foodFrame = tk.Frame(self.entryFrame)
            self.foodFrame.pack(side=tk.LEFT)
            tk.Label(self.foodFrame,anchor="n",text="Enter food:").pack() #default top
            self.foodNameStr = tk.StringVar(self.entryFrame)
            self.enterFoodBox = tk.Entry(self.foodFrame,textvariable=self.foodNameStr)
            self.enterFoodBox.pack(side= tk.BOTTOM)

            #Year widget
            self.yearFrame = tk.Frame(self.entryFrame)
            self.yearFrame.pack(side=tk.LEFT)
            tk.Label(self.yearFrame,anchor="n",text="Enter Year:").pack()
            self.yearNameStr = tk.StringVar(self.entryFrame)
            self.enterYearBox = tk.Entry(self.yearFrame,textvariable=self.yearNameStr)
            self.enterYearBox.pack(side= tk.BOTTOM)


            #Month widget
            self.monthFrame = tk.Frame(self.entryFrame)
            self.monthFrame.pack(side=tk.LEFT)
            tk.Label(self.monthFrame,anchor="n",text="Enter Month:").pack()
            self.monthNameStr = tk.StringVar(self.entryFrame)
            self.enterMonthBox = tk.Entry(self.monthFrame,textvariable=self.monthNameStr)
            self.enterMonthBox.pack(side= tk.BOTTOM)

            #day widget
            self.dayFrame = tk.Frame(self.entryFrame)
            self.dayFrame.pack(side=tk.LEFT)
            tk.Label(self.dayFrame,anchor="n",text="Enter Day:").pack()
            self.dayNameStr = tk.StringVar(self.entryFrame)
            self.enterdayBox = tk.Entry(self.dayFrame,textvariable=self.dayNameStr)
            self.enterdayBox.pack(side= tk.BOTTOM)

            #entry button
            self.entryButton = tk.Button(self.entryFrame,command=self.entryButtonFunction,text='Put food in fridge')
            self.entryButton.pack(side=tk.RIGHT)

        def entryButtonFunction(self):
            apt.writeItemToCsv(self.foodNameStr.get(),self.monthNameStr.get(),self.dayNameStr.get(),self.yearNameStr.get())

            


apt.gui()



