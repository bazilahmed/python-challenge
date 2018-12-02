# program to analyze the poll data and print the results
import csv

file_path = "Resources/election_data.csv"
with open(file_path, newline="") as file_object:
    csv_reader = csv.reader(file_object, delimiter=",")

    header = next(csv_reader)  # to store the header in a list and also move to next line

    voter_ids = []
    counties = []
    candidates = []
    for row in csv_reader:
        voter_ids.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])

# create tuples to store lists values, which are immutable
t_voter_ids = tuple(voter_ids)
t_counties = tuple(counties)
t_candidates = tuple(candidates)

# get the total vote count
total_votes = len(voter_ids)

# use set method to get the unique values in a list/tuple
# convert this set to tuple to make it immutable
t_all_candidates = tuple(set(t_candidates))

# create two more tuples to get the counts and percentages using tuple comprehensions
t_counts = tuple(t_candidates.count(candidate) for candidate in t_all_candidates)
t_percents = tuple(round((t_candidates.count(candidate) / total_votes) * 100, 3)
                   for candidate in t_all_candidates)

# now get the index for the max percentage from the t_percents tuple to find the winner in t_all_candidates
max_count_index = (t_percents.index(max(t_percents)))
winner = t_all_candidates[max_count_index]

# final output
print("Election Results\n" +
      "-------------------------\n" +
      f"Total Votes: {total_votes}\n" +
      "-------------------------")

# use the 3 tuples to print the summary
for x in range(len(t_all_candidates)):
    print(f"{t_all_candidates[x]}: {t_percents[x]}% ({t_counts[x]})")

# print the winner
print("-------------------------\n" +
      f"Winner: {winner}\n" +
      "-------------------------")

# save the output to a text file
with open("Election_Results.txt", "w") as file_object:
    file_object.write(
        "Election Results\n" +
        "-------------------------\n" +
        f"Total Votes: {total_votes}\n" +
        "-------------------------")
    for x in range(len(t_all_candidates)):
        file_object.write(f"\n{t_all_candidates[x]}: {t_percents[x]}% ({t_counts[x]})")
    file_object.write("\n-------------------------\n" +
                      f"Winner: {winner}\n" +
                      "-------------------------")
