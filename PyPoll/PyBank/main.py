#import modules
import os
import csv


# set file path
csv_input = os.path.join("Resources", "budget_data.csv")

# Export to text file
text_path = "output.txt"

# Set variables
net_total = 0
total_months = 0
pl = []
previous = 0
month_change = []
profit_change = 0
greatest_inc = 0
profit_month = ''
greatest_dec = 0
loss_month = ''


# open file
with open(csv_input) as budget_file:
    budget_reader = csv.reader(budget_file)
    headers = next(budget_reader)
    
# Calculate total months
    for x in budget_reader:
        total_months = total_months + 1
        net_total = net_total + int(x[1])
        (int(x[1])/10)
# Calculate the average change profit/losses
        if total_months != 1:
            current_pl = int(x[1]) - previous
            pl.append(current_pl)
        
        previous = int(x[1])
        
# Calculate greatest increase/decrease in profits
        if int(x[1]) > greatest_inc:
            profit_month = (x[0])
            greatest_inc = int(x[1])
        elif int(x[1]) < greatest_dec:
            loss_month = (x[0])
            greatest_dec = int(x[1])
            
            
# export as text file
data = "Output of Data"
with open("output.txt", 'w') as f:
    f.write(data)
        
            
       


# Print out statements
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
# print(pl)
# print(sum(pl))
print(f"Average Change: ${sum(pl)/ len(pl)}")
print("Greatest Increase in Profits: " + str(profit_month) + " ($" + str(greatest_inc) + ")")
print("Greatest Decrease in Profits: " + str(profit_month) + " ($" + str(greatest_dec) + ")")









