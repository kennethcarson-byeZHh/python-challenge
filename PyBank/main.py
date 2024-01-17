#import tools and generate datafram

import pandas as pd

from pathlib import Path

budget = Path("resources/budget_data.csv")

budget_df = pd.read_csv(budget)

#Determine total number of months in dataframe

Date_count = len(budget_df["Date"].unique())
print("Total Months: " + str(Date_count))

#Net total profit/loss over time period
Total = budget_df["Profit/Losses"].sum()
print("Total: " + str(Total))


#Insert a column with difference
Differ = budget_df["Profit/Losses"].diff()
budget_df.insert(2,"Difference", Differ)

#visualize column with Differencejhg
print(budget_df)

#Average Change 
Aver = Differ.mean()

#Round to two digits
Averag = Aver.round(2)
print("Average Change: " + str(Averag))

#Find min and max values of difference

Differ = budget_df["Profit/Losses"].diff()

Max_Differ = int(Differ.max())
Min_Differ = int(Differ.min())
print(Max_Differ)
print(Min_Differ)

#Identify max Date and value
Max_result = budget_df.loc[budget_df["Difference"] == Max_Differ, "Date"]
print("Greatest Increase in Profits: " + str(Max_result) + " ($" + str(Max_Differ) + ")")

#Identify Minimum date and value
Min_result = budget_df.loc[budget_df["Difference"] == Min_Differ, "Date"]
print("Greatest Decrease in Profits: " + str(Min_result) +  " ($" + str(Min_Differ) + ")")

with open("/Users/kennethcarson/Desktop/DataViz/python-challenge/PyBank/analysis/output.txt", 'w') as file:
    file.write("Financial Analysis \n")
    file.write("------------------------------ \n")
    file.write("Total Months: " + str(Date_count) + "\n")
    file.write("Total: " + str(Total) + "\n")
    file.write("Average Change: $" + str(Averag) + "\n")
    file.write("Greatest Increase in Profits: " + str(Max_result) + " ($" + str(Max_Differ) + ")" +"\n")
    file.write("Greatest Decrease in Profits: " + str(Min_result) +  " ($" + str(Min_Differ) + ")" +"\n")

#table for export
print("Financial Analysis")
print("------------------------------")
print("Total Months: " + str(Date_count))
print("Total: " + str(Total))
print("Average Change: $" + str(Averag))
print("Greatest Increase in Profits: " + str(Max_result) + " ($" + str(Max_Differ) + ")")
print("Greatest Decrease in Profits: " + str(Min_result) +  " ($" + str(Min_Differ) + ")")

