#import tools and generate dataframe

import pandas as pd

from pathlib import Path

Poll_data = Path("resources/election_data.csv")

Poll_data_df = pd.read_csv(Poll_data, encoding = "ISO-8859-1")

#Count total number of votes

vote_count = len(Poll_data_df["Ballot ID"])

print("Total Votes:  " + str(vote_count) )

mylist = Poll_data_df["Candidate"]

cand_list = []

for item in mylist:
        if item not in cand_list:
                cand_list.append(item)

print(cand_list)

#Count and percentage CCS
Indiv_count = Poll_data_df["Candidate"].value_counts()["Charles Casper Stockham"]
Percen = Indiv_count/vote_count * 100
Percent = Percen.round(3)
print("Charles Casper Stockham:  " + str(Percent) + "%   (" + str(Indiv_count) + ")")

#Count and percentage DG
Indiv_count_DG = Poll_data_df["Candidate"].value_counts()["Diana DeGette"]
Percen_DG = Indiv_count_DG/vote_count * 100
Percent_DG = Percen_DG.round(3)
print("Diana DeGette:  " + str(Percent_DG) + "%   (" + str(Indiv_count_DG) + ")")

#Count and percentage RAD
Indiv_count_RAD = Poll_data_df["Candidate"].value_counts()["Raymon Anthony Doane"]
Percen_RAD = Indiv_count_RAD/vote_count * 100
Percent_RAD = Percen_RAD.round(3)
print("Raymon Anthony Doane:  " + str(Percent_RAD) + "%   (" + str(Indiv_count_RAD) + ")")

#Final printout
with open("/Users/kennethcarson/Desktop/DataViz/python-challenge/PyPoll/analysis/output.txt", 'w') as file:

    file.write("Election Results \n")
    file.write("---------------------------- \n")
    file.write("Total Votes:  " + str(vote_count) + "\n" )
    file.write("---------------------------- \n")
    file.write("Charles Casper Stockham:  " + str(Percent) + "%   (" + str(Indiv_count) + ")" + "\n")
    file.write("Diana DeGette:  " + str(Percent_DG) + "%   (" + str(Indiv_count_DG) + ")" + "\n")
    file.write("Raymon Anthony Doane:  " + str(Percent_RAD) + "%   (" + str(Indiv_count_RAD) + ")" + "\n")
    file.write("---------------------------- \n")
    file.write("Winner:  Diana DeGette \n")
    file.write("---------------------------- \n")

print("Election Results")
print("----------------------------")
print("Total Votes:  " + str(vote_count) )
print("----------------------------")
print("Charles Casper Stockham:  " + str(Percent) + "%   (" + str(Indiv_count) + ")")
print("Diana DeGette:  " + str(Percent_DG) + "%   (" + str(Indiv_count_DG) + ")")
print("Raymon Anthony Doane:  " + str(Percent_RAD) + "%   (" + str(Indiv_count_RAD) + ")")
print("----------------------------")
print("Winner:  Diana DeGette")
print("----------------------------")