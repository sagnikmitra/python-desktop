valCand = ["A", "B", "C"]
voteCount = ["A", "A", "E", "A", "B", "B", "C", "F"]
dictCand = {"A": 0, "B": 0, "C": 0}
invalidVotes = 0
for i in voteCount:
    if i in valCand:
        dictCand[i] += 1
    else:
        invalidVotes += 1
maxVote = -1
maxVoteCand = ""
for i in dictCand.keys():
    if dictCand[i] > maxVote:
        maxVote = dictCand[i]
        maxVoteCand = i
Winner = ""
if((invalidVotes > maxVote) or (len(voteCount) == 0)):
    Winner += "N/A"
else:
    Winner += str(maxVoteCand)
res = ""
for i in dictCand.keys():
    res += i
    res += "="
    res += str(dictCand[i])
    res += " "
strRES = str(f"{res}{invalidVotes=} {Winner=}")
print(strRES)
