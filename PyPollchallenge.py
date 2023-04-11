import os 
import csv 

file_to_load = os.path.join("Resources", "election_data.csv")
print(file_to_load)
file_to_save = os.path.join("Analysis", "election_data.txt")


total_votes = 0
candidate_options = []
candidate_votes = {}
county_names = []
county_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
largest_county_turnout = ""
largest_county_vote = 0
with open(file_to_load) as PyPoll2:
    csvreader=csv.reader(PyPoll2)
    print(csvreader)

    header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        county_name = row[1]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0 
        candidate_votes[candidate_name] += 1

        if county_name not in county_names:
            county_names.append(county_name)

            county_votes[county_name] = 0 
        county_votes[county_name] += 1

with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nelection_results\n"
        f"..\n"
        f"total votes {total_votes:,}\n"
        f"..\n"
        f"county votes:\n"
    )
    print(election_results, end="")
    txt_file.write(election_results)
    
    for county in county_votes:
        county_vote = county_votes[county]
        county_percent = int(county_vote)/int(total_votes) * 100 
        county_results = (
            f"{county}: {county_percent:1f}% ({county_vote:,})\n"
        )
        print(county_results, end="")
        txt_file.write(county_results)

        if (county_vote > largest_county_vote): 
            largest_county_vote = county_vote
            largest_county_turnout = county 

        largest_county_turnout = (
            f"\n..\n"
            f"largest county turnout {largest_county_turnout}\n"
            f"..\n"
        )
        print(largest_county_turnout)
        txt_file.write(largest_county_turnout)

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = int(votes)/ int(total_votes) *100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
        )

        print (candidate_results)
        txt_file.write(candidate_results)

        if (votes> winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    
    winning_candidate_summary = (
        f"..\n"
        f"Winner:{winning_candidate}\n"
        f"winning_vote_count: {winning_count:,}\n"
        f"..\n"
        )

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)