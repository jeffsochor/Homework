import os
import csv

csv_path = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidate = ""
candidate_votes = {}
candidate_percentages ={}
winner_votes = 0
winner = ""

with open(csv_path) as data:
    reader = csv.reader(data)
    header = next(reader)

    for row in reader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1


for person, vote_count in candidate_votes.items():
    candidate_percentages[person] = '{0:.0%}'.format(vote_count / total_votes)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person


print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for person, vote_count in candidate_votes.items():
    print(f"{person}: {candidate_percentages[person]} ({vote_count})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

saveFile = open("ElectionResults.txt", 'w')
saveFile.write("Election Results" + "\n")
saveFile.write("-----------------------------------" + "\n")
saveFile.write(f"Total Votes: {total_votes}" + "\n")
saveFile.write("-------------------------" + "\n")
for person, vote_count in candidate_votes.items():
    saveFile.write(f"{person}: {candidate_percentages[person]} ({vote_count})" + "\n")
saveFile.write("-------------------------" + "\n")
saveFile.write(f"Winner: {winner}" + "\n")
saveFile.write("-------------------------")
saveFile.close()