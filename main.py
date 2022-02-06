from asyncore import write
import tkinter as tk
import datetime
import pandas as pd
from pandas import read_csv
import csv

shawzub = 1


class apt:

    fridge = 'https://github.com/Ibrahim-gw8885/Aperature/blob/main/fridge.csv'

    def __init__ (self):
        pass
    
    def returnDaysRemaining():
        pass

    def readItemFromCsv():
        with open(apt.fridge, newline='', mode = 'r'):
            for lines in apt.fridge:
                print(lines)
    
    def writeItemToCsv():
        with open(apt.fridge, mode = 'r'):
            for lines in apt.fridge:
                print(lines)

    class gui:
        def __init__(self):
            pass
        
        def inputWidget():
            inputWidgetCol = tk.Frame(root)

apt.writeItemToCsv()