# Import the OS and CSV modules
import os
import csv


# Create file path
csvpath = os.path.join("Resources", "budget_data2.csv")

# Open as a read only file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)


    total_month = 0
    total_amount = 0
    date = []
    profit_losses = []
    monthly_change = []
    

# For loop
    for row in csvreader:
        total_month += 1
        total_amount += int(row[1])
        date.append(row[0])
        profit_losses.append(row[1])
        

     # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    change = int(profit_losses[-1]) - int(profit_losses[0])

    # Reduce Total Months by 1
    count_avg = total_month - 1

    avg_change = change / count_avg
    # Reduce Decimal Places
    limit_dec = round(avg_change, 2)


    # Deermine Greatest Increase in Profits and Greatest Decrease in Losses by Month/Year
    
    for i in range(1, len(profit_losses)):
        change_by_month = int(profit_losses[i]) - int(profit_losses[i-1])
        monthly_change.append(int(change_by_month))
    
    #Greatest Increase (Profits)
    maximum = max(monthly_change)
    maximum_index = monthly_change.index(maximum) + 1
    max_date = date[maximum_index]


    #Greatest Decrease (Losses)
    minimum = min(monthly_change)
    minimum_index = monthly_change.index(minimum) + 1
    min_date = date[minimum_index]
    
    # Print Statements
    print('Financial Analysis')
    print('----------------------')
    print(f"Total Months = {total_month}")
    print(f"Total Amount = ${total_amount}")
    print(f"changes = ${change}")
    print(f"Average Change = ${limit_dec}")
    print(f"Greatest Increase in Profits: {max_date} $({maximum})") 
    print(f"Greatest Decrease in Profits: {min_date} S({minimum})") 

# write terminal output to .txt file
output_path = os.path.join("Analysis", "results.txt")

with open(output_path, 'w') as file:
    file.write('Financial Analysis \n')
    file.write('---------------------- \n')
    file.write(f"Total Months = {total_month} \n")
    file.write(f"Total Amount = ${total_amount} \n")
    file.write(f"changes = ${change} \n")
    file.write(f"Average Change = ${limit_dec} \n")
    file.write(f"Greatest Increase in Profits: {max_date} $({maximum}) \n")
    file.write(f"Greatest Decrease in Profits: {min_date} S({minimum})") 

