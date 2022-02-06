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

    def writeItemToCsv(foodName,exp_date):
        foodName = str(foodName)
        rowWrite = [foodName,exp_date]

        with open(apt.fridge, mode = 'w',newline='') as file:
            csvWriter = csv.writer(file)
            csvWriter.writerow(rowWrite)

    class gui:
        def __init__(self):
            pass
        
        def inputWidget():
            inputWidgetCol = tk.Frame(root)

apt.writeItemToCsv('banannnnnnnnnnna','12-20-2000')