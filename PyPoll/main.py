# import csv and os modules
import os
import csv

# create file path
csvpath = os.path.join("Resources", "election_data2.csv")

# open file as read only
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

# declare variables
    total_votes = 0
    candidates = []
    can_1 = 0
    can_2 = 0
    can_3 = 0
    can_4 = 0

# for loop
    for row in csvreader:
        #count total votes
        total_votes += 1
        #use if statement to create a list of the candidates
        if row[2] not in candidates:
            candidates.append(row[2])
        #use elif to count unique candidate votes    
        if row[2] == candidates[0]:
            can_1 += 1
        elif row[2] == candidates[1]:
            can_2 += 1
        elif row[2] == candidates[2]:
            can_3 += 1
        elif row[2] == candidates[3]:
            can_4 += 1
        

            
    #calculate candidate percentage of vote total
    can1_percentage = int(can_1) / int(total_votes) * 100
    can1_percentage = round(can1_percentage, 2)
    
    can2_percentage = int(can_2) / int(total_votes) * 100
    can2_percentage = round(can2_percentage, 2)

    can3_percentage = int(can_3) / int(total_votes) * 100
    can3_percentage = round(can3_percentage, 2)

    can4_percentage = int(can_4) / int(total_votes) * 100
    can4_percentage = round(can4_percentage, 2)

    # Determine Winner
    candidate_count = [can_1, can_2, can_3, can_4]
    winner = max(candidate_count)
    candidate_count_index = candidate_count.index(winner)
    winner_name = candidates[candidate_count_index]

# print statements:
    print("Election Results \n")
    print("--------------- \n")
    print(f"Total Votes: {total_votes} \n")
    print("--------------- \n")
    print(f"{candidates[0]}: {can1_percentage}% ({can_1}) \n")
    print(f"{candidates[1]}: {can2_percentage}% ({can_2}) \n")
    print(f"{candidates[2]}: {can3_percentage}% ({can_3}) \n")
    print(f"{candidates[3]}: {can4_percentage}% ({can_4}) \n")
    print("--------------- \n")
    print(f"Winner: {winner_name} \n")
    print("--------------- \n")

# Write to a text file
output_path = os.path.join("Analysis", "results.txt")

with open(output_path, 'w') as file:
    file.write("Election Results \n")
    file.write("--------------- \n")
    file.write(f"Total Votes: {total_votes} \n")
    file.write("--------------- \n")
    file.write (f"{candidates[0]}: {can1_percentage}% ({can_1}) \n")
    file.write(f"{candidates[1]}: {can2_percentage}% ({can_2}) \n")
    file.write(f"{candidates[2]}: {can3_percentage}% ({can_3}) \n")
    file.write(f"{candidates[3]}: {can4_percentage}% ({can_4}) \n")
    file.write("--------------- \n")
    file.write(f"Winner: {winner_name} \n")
    file.write("--------------- \n")
