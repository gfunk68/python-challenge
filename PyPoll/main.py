import csv
import os

totalvotes = 0
candidatelist = []
totalvotescandidate = []
maxvote = 0

csvpath = os.path.join("Resources", "election_data.csv")
writepath = os.path.join("Resources", "election_summary.txt")


with open(csvpath) as election_data:
    csvreader = csv.reader(election_data, delimiter=',')

    row = next(csvreader,None)


    for row in csvreader:

        totalvotes = totalvotes + 1
        
        candidate = row[2]

        if candidate in candidatelist:

            totalvotescandidate[candidatelist.index(candidate)] = totalvotescandidate[candidatelist.index(candidate)] +1

        else:
            candidatelist.append(candidate)
            totalvotescandidate.append(1)

        
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes {totalvotes}")
    print("----------------------------")
    for indx in range(len(candidatelist)):
        
        print(f"{candidatelist[indx]} {round((totalvotescandidate[indx]/totalvotes)*100,2)} % ({totalvotescandidate[indx]})") 
        if totalvotescandidate[indx] > maxvote:
            maxvote = totalvotescandidate[indx]
            winner = candidatelist[indx] 
    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")

    with open(writepath, "w", newline ='') as txtfile:
        txtfile.write("Election Results\n")
        txtfile.write("----------------------------\n")
        txtfile.write(f"Total Votes {totalvotes}\n")
        txtfile.write("----------------------------\n")   
        for indx in range(len(candidatelist)):
            txtfile.write(f"{candidatelist[indx]} {round((totalvotescandidate[indx]/totalvotes)*100,2)} % ({totalvotescandidate[indx]})\n") 
        txtfile.write("----------------------------\n")
        txtfile.write(f"Winner: {winner}\n")
        txtfile.write("----------------------------\n")