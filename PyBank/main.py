# Import what I need
import os
import csv

# Construct path to pull data from
budget_csv = os.path.join('resources', 'budget_data.csv')

# Define the funtion to be called to run the analysis
def print_financial_analysis(budget_data): #Figure out what my parameters should be if any
    #Create variables to store key information
    months = 0 #can we just rely on the number of rows minus that for the header?
    total = 0
    average_change = 0
    first_amount = 0
    last_amount = 0
    greatest_increase = 0
    greatest_increase_month = ""
    greatest_decrease = 0
    greatest_decrease_month = ""
    previous_amount = None

    #Iterate through the budget data and keep track of key information
    for row in budget_data:
        months += 1
        total += int(row[1])

        #Record first amount value and last amount value
        if months == 1:
            first_amount = int(row[1])
        elif months == 86: #Does this need to be dynamic?
            last_amount = int(row[1])

        #Condition on whether there is a previous amount by checking if the value is none
        if previous_amount is not None:
            #calculate the change from prev to curr 
            current_change = int(row[1]) - previous_amount
            if current_change < greatest_decrease or current_change > greatest_increase:
                if current_change < 0:
                    greatest_decrease = current_change
                    greatest_decrease_month = row[0]
                elif current_change > 0:
                    greatest_increase = current_change
                    greatest_increase_month = row[0]

        #This needs to be the last thing done in the for loop so I don't mess it up
        previous_amount = int(row[1])

    #Calculate average change - not sure how TODO this
    # delta y / delta x = (y2 - y1)/(x2 - x1) = (Last total - first total)/(last month count - first month)
    average_change = (last_amount - first_amount)/(months - 1)

    #Print out the key insights
    print("Financial Analysis")
    print("------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${round(average_change, 2)}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

    #Export the same information to an additional file in the analysis folder
    
    file = open("analysis/budget_analysis.txt", "w")
    file.write("Financial Analysis\n")
    file.write("-------------\n")
    file.write(f"Total Months: {months}\n")
    file.write(f"Total: ${total}\n")
    file.write(f"Average Change: ${round(average_change, 2)}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

#Read in the csv file
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader) #This is the header data and this function pushes us to the first row of real data

    #call function and then loop through the data since we want its aggregated information
    print_financial_analysis(csvreader)