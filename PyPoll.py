#Add dependencies
import os
import csv
#assign a variable to the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
#Create a file name variable for output file
file_to_save = os.path.join("Analysis","election_analysis.txt")

# open the election results file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #read and print header row
    headers = next(file_reader)
    print(headers)







