from asyncore import write
import tkinter as tk
import datetime
import pandas as pd
from pandas import read_csv
import csv

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

apt.writeItemToCsv('milk','12-20-2000')
apt.readAllItemsFromCsv()
apt.returnFoodAndExp('milk')
