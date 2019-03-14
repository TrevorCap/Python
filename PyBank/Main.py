import os
import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline="") as budget:
    csvreader = csv.reader(budget, delimiter=",")
    budget.readline()
    total = 0
    rows = 0
    MaxV = 0
    MaxD = ""
    MinV = 0
    MinD = ""
    change = 0
    Taverage = 0
    val1 = 0
    val2 = 0

    for row in csv.reader(budget):
        total += int(row[1])
        rows += 1 
        val1 = int(row[1])       
        change = val1 - val2
        if rows > 1:
            Taverage += change

        if change > MaxV:
            MaxV = change
            MaxD = row[0]
        
        if change < MinV:
            MinV = change
            MinD = row[0]
        val2 = val1
      
Taverage = round(Taverage/(rows-1), 2)
print("Financial Analysis", file=open('Output.txt', "a"))
print("-----------------------------------------------------", file=open('Output.txt', "a"))
print("Total Months: ", rows, file=open('Output.txt', "a"))
print("Total: $", total, file=open('Output.txt', "a"))
print("Average Change: $", Taverage, file=open('Output.txt', "a"))   
print("Greatest increase in profits: ", MaxD, " ($", MaxV, ")", file=open('Output.txt', "a")) 
print("Greatest decrease in profits: ", MinD, " ($", MinV, ")", file=open('Output.txt', "a")) 
print("Financial Analysis")
print("-------------------------------")
print("Total Months: ")
print("Total: $")
print("Average Change: $", Taverage)   
print("Greatest increase in profits: ", MaxD, " ($", MaxV, ")") 
print("Greatest decrease in profits: ", MinD, " ($", MinV, ")") 