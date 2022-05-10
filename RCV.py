#import libraries
import csv
import math
import pyrankvote
from pyrankvote import Candidate, Ballot

#open the file and put it into a list
with open("dummydata4dummies.csv") as data:
    read = csv.reader(data)
    votes = list(read)

#assign each persons votes to a unique identifier, I used email as the unqiue identifier
votesdict = {}
for i in range(1, len(votes)):
    votesdict[votes[i][1]] = votes[i][5:12]

#weightage calculation
weightage = {}
nonmentor = 0
mentor = 0

#make a dictionary lookup based on email for weightage
for i in range(1, len(votes)):
    if (votes[i][4] == "First year"):
        weightage[votes[i][1]] = 2
        nonmentor += 2
    if (votes[i][4] == "Second year"):
        weightage[votes[i][1]] = 3
        nonmentor += 3
    if (votes[i][4] == "Third or fourth year"):
        weightage[votes[i][1]] = 4
        nonmentor += 4
    if (votes[i][4] == "Mentor"):
        mentor += 1

#calculate mentor share and assign
for i in range(1, len(votes)):
    if votes[i][4] == "Mentor":
        weightage[votes[i][1]] = math.ceil((nonmentor / 4) / mentor)

#create candidate objects
cole = Candidate("Cole Massie")
emi = Candidate("Emi Hiroshima")
jacob = Candidate("Jacob Jurek")
leison = Candidate("Leison Gao")
max = Candidate("Max Schleicher")
theadin = Candidate("Theadin Bachman")

#candidate list for later use by library
candidates = [cole, emi, jacob, leison, max, theadin]

#dictionary conversion from spreadsheet input to candidate object
candict = {"Cole Massie": cole, "Emi Hiroshima": emi, "Jacob Jurek": jacob, "Leison Gao": leison, "Max Schleicher": max, "Theadin Bachman":theadin}

#factoring in weightage, this reads all the mechanical ballots
ballots = []
for i in votesdict:
    for k in range(weightage[i]):
        ballots.append(Ballot(ranked_candidates=[candict[j] for j in votesdict[i][0:5]]))

#find election result using library
election_result = pyrankvote.instant_runoff_voting(candidates, ballots)
print(election_result)

#The exact same process detailed in mechanical is repeated with different variables for programming
richie = Candidate("Richie Tan")
michael = Candidate("Michael Kersey")
anthony = Candidate("Anthony Furman")
progcand = [richie, michael, anthony]
progball = []
progdict = {"Richie Tan": richie, "Michael Kersey": michael, "Anthony Furman": anthony}
for i in votesdict:
    for k in range(weightage[i]):
        progball.append(Ballot(ranked_candidates=[progdict[j] for j in votesdict[i][5:8]]))

prog_result = pyrankvote.instant_runoff_voting(progcand, progball)
print(prog_result)

#and we're done!
print("---")
print("Joseph R. Biden Jr wins the 2020 Presidential Election")




