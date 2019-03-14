import os
import csv
from collections import Counter

csvpath = os.path.join('elections.csv')
counters = []
with open(csvpath, newline="") as votes:
    csvreader = csv.reader(votes, delimiter=",")
    votes.readline()
    votes = 0


    for row in csv.reader(votes):
        votes += 1
        for colno,datum in enumerate(row):
            if colno >= len(counters):
                counters.append( Counter()  )
            counters[colno][datum] += 1

# file=open('Output.txt', "a")
print("Election Results")
print("-------------------------")
print("Total Votes: ", votes)
print("-------------------------")

#category = counters[]
#char, num = counter(counters).most_common(1)[0]
#print( char, num)
print(counters)