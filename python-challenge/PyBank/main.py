#import extensions

import os
import csv

csvpath = os.path.join('resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    print (csvreader)