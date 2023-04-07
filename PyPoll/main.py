# import modules
import os
import csv

# set file path
csv_input = os.path.join("Resources", "election_data.csv")

# export file as text file
file_output = "election.txt"

# set variables

total_votes = 0
net_total = 0
candidates = []
candidate = []
candidate_votes = {}
winner = ""
winner_total = 0
voters = {}


# open file
with open(csv_input) as election_file:
    election_reader = csv.reader(election_file)
    headers = next(election_reader)
# calculate total votes
    for x in election_reader:
        total_votes += 1
        if x[2] not in candidate_votes:
            candidate_votes[x[2]] = 1
        else:
            candidate_votes[x[2]] += 1
        
# list of candidates who received votes
    for x in election_reader:
        if x[3].strip() not in candidates:
            candidates.append(x[2])
        else:
            continue
            
 

#Find the winner
# winner = max(candidates.values(0))
# winner = list(voters.keys())[list(voters.vaules()).index(winner_total)        
# find the winner
# for candidate in candidates:
# total_votes = 0
# for x in election_reader:
# if x[2] == candidate:
# total_votes +=1
# voters[candidate] = total_votes
# winner_vote = max(voters.values())
# winner = list(voters.keys())[list(voters.values()).index(winner_vote)]
   
       
# export as text file
data = "Output of Data"
with open("election.txt", 'w') as f:
    f.write(data)    
       
    
    
    
print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")
print(str(candidate) + str(candidate_votes))
print("Winner: Diana DeGette")
