# Election_Analysis
## Overview

The purpose of this analysis is to find out which candidate won the election and which county had the highest turnout. I performed this analysis by using Python to read and modify data from a .csv file (election_results). I wrote the results of the election to a .txt file (election_analysis).

## Election Results

![Election_Results](https://github.com/jolwig/Election_Analysis/blob/main/analysis/election_analysis.txt)

        County Votes:
        Jefferson: 10.5% (38,855)
        Denver: 82.8% (306,055)
        Arapahoe: 6.7% (24,801)
        Largest County Turnout: Denver

Denver had the largest voter turnout by a wide margin. It made up for 82.8% of the total vote count. Arapahoe had the lowest turnout with only 6.7% of the total vote count.

        Candidate Votes:
        Charles Casper Stockham: 23.0% (85,213)
        Diana DeGette: 73.8% (272,892)
        Raymon Anthony Doane: 3.1% (11,606)
        Winner: Diana DeGette

Diana DeGette won by a wide margin with 73.8% of the total votes. Raymon Anthony Doane had the fewest votes with only 3.1% of the total votes.

## Summary

The Python script that was used for this analysis can be reused for analysing other elections. The only change that would need to be made is the "file_to_load" variable would have to be replaced with the correct file path.
