import pandas as pd
import numpy as np

votes = "elections.csv"
vote = pd.read_csv(votes)
vote2 = pd.concat([vote.Candidate.value_counts(), 
                round(vote.Candidate.value_counts(normalize=True).mul(100),1)],axis=1, keys=("Votes", "%"))
voted = len(vote.index)
winner = vote.Candidate.mode().iloc[0]

# file=open('Output.txt', "a")
print("Election Results")
print("-------------------------")
print("Total Votes: ", voted)
print("-------------------------")
print(vote2.to_string(index = True))
print("-------------------------")
print("Winner: ", winner)
print("-------------------------")

print("Election Results", file=open('Output.txt', "a"))
print("-------------------------",file=open('Output.txt', "a"))
print("Total Votes: ", voted, file=open('Output.txt', "a"))
print("-------------------------",file=open('Output.txt', "a"))
print(vote2.to_string(index = True), file=open('Output.txt', "a"))
print("-------------------------", file=open('Output.txt', "a"))
print("Winner: ", winner, file=open('Output.txt', "a"))
print("-------------------------", file=open('Output.txt', "a"))