#import dependencies
import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('..','Resources','election_data.csv')
# Create Variables 
listOfCandidates = []
listOfTotals = []
voteCount = 0
candidatePosition = 0
candidateCount = 0
totalVotes = 0
winnerVotes = 0
nameOfWinner = ""
percentVotesPerCandidate = []
#noOfTimesCandidatesAppearInList = total votes gained by each candidate
# open File for read only

with open('election_data.csv', 'r') as csvfile:
      
      csv_reader = csv.reader(csvfile,  delimiter = ',')
      header = next(csv_reader)
      first_row = next(csv_reader)
      listOfCandidates.append(first_row[2])
      listOfTotals.append(1)
      voteCount = voteCount + 1
      for row in csv_reader:
        #row_count = sum(1 for row in csvfile)
        if(row[2] not in listOfCandidates ):
            listOfCandidates.append(row[2])
            listOfTotals.append(1)
        else:
            candidatePosition = listOfCandidates.index(row[2])
            listOfTotals[candidatePosition] += 1

      nameOfWinner = listOfCandidates[0]
      winnerVotes = listOfTotals[0]
      while candidateCount < len(listOfCandidates):
          print(f"Candidate Name: {listOfCandidates[candidateCount]}, Total Votes Secured: {listOfTotals[candidateCount]}")
          totalVotes += listOfTotals[candidateCount]
          if listOfTotals[candidateCount] > winnerVotes:
              nameOfWinner = listOfCandidates[candidateCount]
              winnerVotes = listOfTotals[candidateCount]
          candidateCount += 1
          print()
      print(f"Total Votes: {totalVotes}")
      print(f"Winner Name: {nameOfWinner}")

      candidateCount = 0
      while candidateCount < len(listOfCandidates):
          print(f"Candidate Name: {listOfCandidates[candidateCount]}, % Votes Secured: {listOfTotals[candidateCount]/totalVotes*100}")
          candidateCount += 1
          print()
          #percentVotesPerCandidate.append = (listOfTotals[candidateCount]/totalVotes*100)
          
# to print to a output txt file
with open('output.txt','a')as txtfile:
    txtfile.write("\nElection Results")  
    txtfile.write("\n--------------------------------------------------------------")
    txtfile.write("\nTotal Votes Cast     :")
    txtfile.write(str(totalVotes))
    txtfile.write("\nWinner Name  :")
    txtfile.write(nameOfWinner) 
    txtfile.write("\nList of Candidates ")
    txtfile.write("\n ")
    candidateCount = 0
    while candidateCount < len(listOfCandidates):
          txtfile.write("Candidate Name: "+listOfCandidates[candidateCount]+" Votes Secured: "+str(listOfTotals[candidateCount]/totalVotes*100)+"% ("+str(listOfTotals[candidateCount])+")")
          candidateCount += 1
          txtfile.write("\n ")
    txtfile.write("\n--------------------------------------------------------------")
txtfile.close()
      
          
