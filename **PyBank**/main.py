# program to analyze the financial records of a company and provide a summary of the analysis as output

import csv

file = "Resources/budget_data.csv"

# open csv file and read it's contents
with open(file, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)  # this is to skip the header and also store in a variable
    # print(header)
    dates = []
    amounts = []

    # use the csv_reader iterator to store the dates and amounts in two separate lists
    for row in csv_reader:
        # print(row)
        dates.append(row[0])
        amounts.append(int(row[1]))

# total number of months included in the dataset
total_months = len(dates)

# total net amount of profits or losses over the entire period
total_amount = sum(amounts)

# average change in profits or losses between months over the entire period
changed_amounts = []
for x in range(1, total_months):
    change = amounts[x] - amounts[x - 1]
    changed_amounts.append(change)

avg_change = round(sum(changed_amounts) / len(changed_amounts), 2)

# greatest increase in profits (date and amount) over the entire period
# find the index from changed amounts and use it to find the relevant element from dates list
greatest_increase = max(changed_amounts)
i = changed_amounts.index(greatest_increase)

grt_incr_date = dates[i + 1]  # adding +1 as the changed_amounts list is offset by 1

# greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(changed_amounts)
i = changed_amounts.index(greatest_decrease)

grt_decr_date = dates[i + 1]  # adding +1 as the changed_amounts list is offset by 1


# final output
print("Financial Analysis\n" +
      "--------------------------------")
print(f"Total Months: {total_months}")
print(f"Total Net Amount: ${total_amount}")
print(f"Average  Change: ${avg_change}")
print(f"Greatest Increase in Profits: {grt_incr_date} (${greatest_increase})")
print(f"Greatest Descrease in Profits: {grt_decr_date} (${greatest_decrease})")

# saving output to a text file
output_file = "PyBank_Analysis.txt"
with open(output_file, "w") as file_object:
    file_object.write("Financial Analysis\n" +
                      "--------------------------------" +
                      "\nTotal Months: " + str(total_months) +
                      "\nTotal Net Amount: $" + str(total_amount) +
                      "\nAverage  Change: $" + str(avg_change) +
                      "\nGreatest Increase in Profits: " + grt_incr_date + " ($" + str(greatest_increase) + ")" +
                      "\nGreatest Descrease in Profits: " + grt_decr_date + " ($" + str(greatest_decrease) + ")")
