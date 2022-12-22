import os
import csv

#path to collect data
election_data = os.path.join('Resources', 'election_data.csv')

#variables to store voter count
count_diana = 0
count_raymon = 0
count_charles = 0

#Lists to store our data
voter_id = []
all_candidate = []
unique_candidate = []

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next (csvreader)

    #loops through and adds values to lists from csv file
    for row in csvreader:
        voter_id.append(int(row[0]))
        all_candidate.append(row[2])

        #loops through and finds unique candidate names and assigns it to unique_candidate list
        candidate = row[2]
        if candidate not in unique_candidate:
            unique_candidate.append(candidate)

#loops through and assigns vote for each candidate accordingly
for i in all_candidate:
    if i == "Raymon Anthony Doane":
        count_raymon = count_raymon + 1

    elif i == "Charles Casper Stockham":
        count_charles = count_charles + 1

    else:
        count_diana = count_diana + 1

# counts total votes, and percentages of votes for each candidate
total_votes = (len(voter_id))
percent_diana = str(round(count_diana/total_votes * 100, 3)) + "%"
percent_raymon = str(round(count_raymon/total_votes * 100, 3)) + "%"
percent_charles = str(round(count_charles/total_votes * 100, 3)) + "%"

#assigns winner to a variable called winner
if percent_diana < percent_raymon and percent_charles < percent_raymon:
    winner = "Raymon Anthony Doane"

elif percent_raymon < percent_diana and percent_charles < percent_diana:
    winner = "Diana DeGette"

else:
    winner = "Charles Casper Stockham"

print("Election Results")
print("-------------------")
print(f"Total votes: {total_votes}")
print("-------------------")
print(f"Charles Casper Stockham: {percent_charles} ({count_charles})")
print(f"Diana DeGette: {percent_diana} ({count_diana})")
print(f"Raymon Anthony Doane: {percent_raymon} ({count_raymon})")
print("-------------------")
print(f"Winner: {winner}")
print("-------------------")

with open ('./analysis.txt' , 'w') as file:

    file.write("Election Results\n")
    file.write("-------------------\n")
    file.write(f"Total votes: {total_votes}\n")
    file.write(f"-------------------\n")
    file.write(f"Charles Casper Stockham: {percent_charles} ({count_charles})\n")
    file.write(f"Diana DeGette: {percent_diana} ({count_diana})\n")
    file.write(f"Raymon Anthony Doane: {percent_raymon} ({count_raymon})\n")
    file.write("-------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------\n")
    file.close()