#import needed modules
import os
import csv

#define the path for the needed PyPollcsv file
PyPollfile = os.path.join('Resources, election_data.csv')
#define the path to write the results to
PyPollfile_output = os.path.join("analysis","election_analysis.txt")
#print(PyPollfile)

#open and read the file
PyPollfile = open("election_data.csv", "r")
#locate the header
electiondata = csv.reader(PyPollfile)
#read the header
next (electiondata)
#print(electiondata)

total_votes = 0
#create a candidate dictionary
candidates = {}

#read through rows
for row in electiondata:
   
#what is the vote count
    total_votes = total_votes + 1
   
    name = row[2]
    #to prevent hard coding, create a way to add in new candidates
    if name not in candidates:
        candidates[name] = 1
    else:
        candidates[name] = candidates[name] + 1
         
#print(total_votes)

#for candidate_name, vote_count in candidates.items():
 #   percentage = round(((vote_count / total_votes) * 100), 2)
  #  print(f"{candidate_name}:  {vote_count}, {percentage}")
#print(candidates)
    
#Who is the winner
max_votes = 0

for candidate_name, vote_count in candidates.items():
    if vote_count > max_votes:
        max_votes = vote_count

        most_candidate_name = candidate_name
#print(most_candidate_name)

#print statements
print(f"Election Results")
print(f"__________________")
print(f"Total Votes:  {total_votes}")
print(f"__________________")
for candidate_name, vote_count in candidates.items():
    percentage = round(((vote_count / total_votes) * 100), 2)
    print(f"{candidate_name}:  {percentage:.3f}%, ({vote_count})")
print(f"__________________")
print(f"Winner: {most_candidate_name}")

#Export to a text file with results
Pypollfile = os.path.join("output", "election_data")
with open("election.txt", "w") as outfile:
    outfile.write(f"Election Results" + "\n")
    outfile.write(f"__________________" + "\n")
    outfile.write(f"Total Votes:  {total_votes}" + "\n")
    outfile.write(f"__________________" + "\n")
    for candidate_name, vote_count in candidates.items():
        percentage = round(((vote_count / total_votes) * 100), 2)
        outfile.write(f"{candidate_name}:  {percentage:.3f}%, ({vote_count})" + "\n")
    outfile.write(f"__________________" + "\n")
    outfile.write(f"Winner: {most_candidate_name}" +"\n")
