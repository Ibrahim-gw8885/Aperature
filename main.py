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
            csvFile = csv.reader(file)
            for lines in csvFile:
                print(lines)

    
    
    def writeItemToCsv():
        with open(apt.fridge, mode = 'w') as file:
            csvFile = csv.writer(file)
                

    class gui:
        def __init__(self):
            pass
        
        def inputWidget():
            inputWidgetCol = tk.Frame(root)

apt.writeItemToCsv()