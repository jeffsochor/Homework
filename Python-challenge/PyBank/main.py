import csv
import os

csv_path = os.path.join("Resources", "budget_data.csv")

revenue = []
date = []
rev_change = []

with open(csv_path) as data:
    reader = csv.reader(data)
    header = next(reader)
    for row in reader:
        revenue.append(int(row[1]))
        date.append(row[0])

    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])
        avg_rev_change = sum(rev_change)/len(rev_change)
        max_rev_change = max(rev_change)
        min_rev_change = min(rev_change)
        max_rev_change_date = str(date[rev_change.index(max(rev_change)) + 1])
        min_rev_change_date = str(date[rev_change.index(min(rev_change)) + 1])
        
print("Financial Analysis")
print("-----------------------------------")
print("Total Months:", len(date))
print("Total: $", sum(revenue))
print("Avereage Change: $",round(avg_rev_change))
print("Greatest Increase in Profits", max_rev_change_date,"($",max_rev_change,")")
print("Greatest Decrease in Profits:", min_rev_change_date,"($",min_rev_change,")")


saveFile = open("FinancialAnalysis.txt", 'w')
saveFile.write("Financial Analysis" + "\n")
saveFile.write("-----------------------------------\n")
saveFile.write("Total Months:" + str(len(date))+"\n")
saveFile.write("Total: $" + str(sum(revenue))+"\n")
saveFile.write("Avereage Change: $" + str(round(avg_rev_change))+"\n")
saveFile.write("Greatest Increase in Profits" + str(max_rev_change_date) + "($" + str(max_rev_change) + ")" +"\n")
saveFile.write("Greatest Decrease in Profits:" + str(min_rev_change_date)+ "($" + str(min_rev_change) + ")")
saveFile.close()