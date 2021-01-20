# import csv and os modules
import os
import csv

# create file path
csvpath = os.path.join("Resources", "election_data2.csv")

# open file as read only
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    