# Election Analysis

## Project Overview
The Colorado election committee has requested additional information on top of the recent analysis completed 
for them in regards to the election analysis.  The board committee would now also like to determine the following:
1.  The voter turnout for each county
2.  the percentage of votes from each county out of the total count
3.  The county with the highest turn out

The challenge is to use Python on the provided Election_results.csv file to calculate the desired statitics and print out the results to the terminal as well as in a text file that can be provided to the election committee.

### Background
Colorado Board of Elections employees, Seth and Tom, have asked for an analysis of election results in 
conjunction with an audit that is being done of a recent local congressional election.  The audit originally requested
the following information:

1.  The Total number of Votes cast
2.  A Complete list of candidates who received votes
3.  The total number of votes each candidate received
4.  What is the percentage of votes each candidate won
5.  Who is the winner of the election by the popular vote

After reviewing this information, the election committee has requested additional information with regards to the individual county showings.  The challenge is to enhance the starter code which developed the audit information to also include the additional request.    

### Resources provided
- Data Source:  election_results.csv
- Software:  Python 3.6.1, Visual Studio code

## Summary

### Election-Audit Results
* THE NUMBER OF TOTAL VOTES CAST IN THIS CONGRESSIONAL ELECTION
>In order to calculate the total votes cast in the election, we used a `for` loop coupled with a `counter variable` that increases each time the `for` loop goes through the rows of data. 
The results of this loop code shows the total votes cast as follows:

![](https://github.com/xactuary/PyPoll-Python-Challenge/blob/master/Resources/total%20votes.PNG)

* BREAKDOWN OF VOTES BY COUNTY AND PERCENTAGE BY COUNTY
>In order to calculate the breakdown of votes by county, a dictionary and list are created to keep county names as the key and accumulated votes by county as the value:

![](https://github.com/xactuary/PyPoll-Python-Challenge/blob/master/Resources/county%20code%201.PNG)
 >Next while still in the `for` loop looking at all the records, when a new county name is encountered it is `append`ed to the the list
 
 ![](https://github.com/xactuary/PyPoll-Python-Challenge/blob/master/Resources/county%20code%202.PNG)
 
 >Finally a new variable to track votes by county is created and increased each time the county name shows up in the data file.
 The percentage of total votes for each county is now easy to calculate by dividing the total of the county by the overall total. 
 
 ![](https://github.com/xactuary/PyPoll-Python-Challenge/blob/master/Resources/county%20percentage.PNG)
 
 * THE COUNTY WITH THE LARGEST VOTES
  >
 
 
 
 
 





