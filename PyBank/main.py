import os
import csv
import math

totalprofit = 0
totalmonths = 0
lastloss = 0
monthofchange = []
maxincreaseprofit = 0
maxdecreaseprofit = 0
profitchange = 0
profitchangelist = []

csvpath = os.path.join('Resources','budget_data.csv')
writecsvpath = os.path.join('Output','budget_summary.txt')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    maxVal = []
    csv_header = next(csvreader)
    for row in csvreader:
        
        totalprofit = totalprofit + int(row[1])
        
        totalmonths = totalmonths + 1

        profitchange = int(row[1]) - lastloss
        profitchangelist.append(profitchange)
        lastloss = int(row[1])
        monthofchange = monthofchange + [row[0]]

        if (profitchange > maxincreaseprofit):
            maxincreaseprofit = profitchange
            maxincreasemonth = row[0]
        
        if (profitchange < maxdecreaseprofit):
            maxdecreaseprofit = profitchange
            maxdecreasemonth = row[0]

profitavg = round(sum(profitchangelist) / len(profitchangelist),2)

print(f"Total Months: {totalmonths}")
print(f"Total: ${totalprofit}")
print(f"Average Change: ${profitavg}")
print(f"Greatest Increase in Profits: {maxincreasemonth} (${maxincreaseprofit})")
print(f"Greatest Decrease in Profits: {maxdecreasemonth} (${maxdecreaseprofit})")

with open(writecsvpath, "w", newline ='') as txtfile:
    txtfile.write(f"Total Months: {totalmonths} \n")
    txtfile.write(f"Total: ${totalprofit} \n")
    txtfile.write(f"Average Change: ${profitavg} \n")
    txtfile.write(f"Greatest Increase in Profits: {maxincreasemonth} (${maxincreaseprofit})\n")
    txtfile.write(f"Greatest Decrease in Profits: {maxdecreasemonth} (${maxdecreaseprofit})\n")