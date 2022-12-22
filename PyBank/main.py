import os
import csv

#path to collect data
budget_data = os.path.join('Resources', 'budget_data.csv')

#Lists to store our data
month = []
profit_loss = []
profit_change = []

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next (csvreader)

    #adds columns from csvfile and stores them into lists
    for row in csvreader:
        month.append(row[0])
        profit_loss.append(int(row[1]))

#finds total months
total_months = len(month)

#finds net profit
net_profit = sum(profit_loss)

#loops through and subtracts current months' value from previous ones
for i in range(1, len(profit_loss)):
    profit_change.append(profit_loss[i] - profit_loss[i-1])
    
#finds avg of changes from previous loop
avg_change = sum(profit_change) / len(profit_change)

#calculates max and stores it
max = profit_change.index(max(profit_change))
greatest_inc = (f"{month[max + 1]} (${profit_change[max]})")

#calculates min and stores it
min = profit_change.index(min(profit_change))
greatest_dec = (f"{month[min + 1]} (${profit_change[min]})")

print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {greatest_inc}")
print(f"Greatest Decrease in Profits: {greatest_dec}")

with open ('./analysis.txt' , 'w') as file:

    file.write("Financial Analysis\n")
    file.write("--------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_profit}\n")
    file.write(f"Average Change: ${avg_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_inc}\n")
    file.write(f"Greatest Decrease in Profits: {greatest_dec}\n")
    file.close()
