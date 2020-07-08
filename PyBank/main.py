#Create a Python script that analyzes the provided data to calculate each of the following:
    #Total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #The average of the changes in "Profit/Losses" over the entire period
    #The greatest increase in profits (data and amount) over the entire period
    #The greatest decrease in profits (data and amount) over the entire period

# Import needed modules 
import os 
import csv

# define the path for the needed PyBankcsv file
PyBankfile = os.path.join('/Resources, budget_data.csv')
# Open and read the file
PyBankfile = open("budget_data.csv", "r")
budget = csv.reader(PyBankfile)
#print (budget)
next (budget)

# Define PyBank Variables
month = []
income = []
income_change = []
monthly_change = []

# Read through each row, one by one
for row in budget:
    #count each row for total dates
    month.append(row[0])
    #print(month)
    #count each row to total PnL total
    income.append(int(row[1]))
#print(len(month)) 
month_total = (len(month))
#print(month_total)
#the sum and ave for PnL 
sum_income = sum(income)
#print(sum_income)
#Ave income Change
i = 0
for i in range(len(income) -1):
    PnL_change = int(income[i+1]) - int(income[i])
    #print(PnL_change)
    income_change.append(PnL_change)
#print(income_change)
    Total_change = sum(income_change)
#print(Total_change)
    average_change = Total_change / len(income_change)
#print(average_change)

# > Increase & Decrease
highest_change = max(income_change)
#print(highest_change)
hm = income_change.index(highest_change)
highest_month = month[hm+1]
#print(highest_month)
lowest_change = min(income_change)
#print(lowest_change)
lm = income_change.index(lowest_change)
lowest_month = month[lm+1]
#print(lowest_month)

#Print Total number of months and net total profit and loss w/required header and line seperation
print("Fianancial Analysis" + "\n")
print("----------------------------" + "\n")
print("Total Months:{}".format(len(month))) 
print("Total: ${}".format(sum(income)))
print(f"Average Change: ${average_change:.2f}".format(sum(income)))
print(f"Greatest Increase in Profits: {highest_month}  (${highest_change})")
print(f"Greatest Decrease in Loses: {lowest_month}  (${lowest_change})")

#Export to a text file with results
budget = os.path.join("output", "budget_data")
with open("budget.txt", "w") as outfile:

    outfile.write("Financial Analysis" + "\n")
    outfile.write("----------------------------" + "\n")
    outfile.write(f"Total Months: {month_total}" + "\n")
    outfile.write(f"Total: ${sum_income}" + "\n") 
    outfile.write(f"Average Change: ${average_change:.2f}"  "\n")
    outfile.write(f"Greatest Increase in Profits: {highest_month}  (${highest_change})" + "\n")
    outfile.write(f"Greatest Decrease in Loses: {lowest_month}  (${lowest_change})")



