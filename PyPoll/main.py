import os
import csv

#Two functions: one for the opening csv, one for handling the data

#Construct path
election_csv = os.path.join("resources", "election_data.csv")

def print_election_analysis(election_data):
    #Initialize variables
    total = 0
    candidates = {}
    curr_most_votes = 0
    winner = ""

    #loop through the data
    for row in election_data:
        if row[2] in candidates:
            candidates[row[2]] += 1
            total += 1
        elif row[2] not in candidates:
            candidates[row[2]] = 1
            total += 1
    
    #Iterate through dictionary to see who is the winner
    for candidate in candidates.keys():
        if candidates.get(candidate) > curr_most_votes:
            curr_most_votes = candidates.get(candidate)
            winner = candidate

    #Print analysis
    print("Election Results")
    print("----------------")
    print(f"Total Votes: {total}")
    print("----------------")
    for candidate in candidates.keys():
        percent_of_votes = candidates.get(candidate)/total * 100
        print(f"{candidate}: {round(percent_of_votes, 3)}% ({candidates.get(candidate)})")
    print("----------------")
    print(f"Winner: {winner}")
    print("----------------")

    #Output analysis
    file = open("analysis/election_analysis.txt", "w")
    file.write("Election Results\n")
    file.write("-------------\n")
    file.write(f"Total Votes: {total}\n")
    file.write("-------------\n")
    for candidate in candidates.keys():
        percent_of_votes = candidates.get(candidate)/total * 100
        file.write(f"{candidate}: {round(percent_of_votes, 3)}% ({candidates.get(candidate)})\n")
    file.write("-------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------")

with open(election_csv, "r") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    header = next(csvreader)
    print_election_analysis(csvreader)