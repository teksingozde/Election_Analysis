# Election_Analysis

## Project Overview

The Colorado Board of Elections has requested an election audit of a recent local congressional election with the following:

1.	Calculation of the total number of votes cast.
2.	A complete list of the candidates who received votes.
3.	Calculation of the total number of votes each candidate received.
4.	Calculation of the percentage of votes each candidate won.
5.	Declaration of the winner of the election based on the popular vote.

### Resources

*	Data Source: election_results.csv
*	Software: Python 3.9.12, Visual Studio Code 1.70.2

## Overview of Election - Audit 

The following items are included in line with the information requested by the Colorado Electoral Board.
* List of districts in the region, 
* The percentage of votes each county has,
* The total number of votes each county has and
* Determining the name of the elector with the highest number of votes in choice is the number of votes it received and the percentage of success.

### Election - Audit Results

In order to analyze the selection results, a code was written in the Python programming language and this code was run on the terminal. The output of the selection analysis is as seen below.

<img width="381" alt="Election_Results_Printed" src="https://user-images.githubusercontent.com/26927158/193119061-b7f871b1-f8b2-4972-9dc9-13d61be57e6c.png">

To analyze the result,

1. The total number of votes cast in this election is 369,711.

2. On a county-by-county basis, the percentile order is:
* Denver (82.8%) - 306,055 votes,
* Jefferson (10.5%) - 38,855 votes,
* Arapahoe (6.7%) - 24,801 votes.

3. The county with the highest votes was Denver.

4. Ranking from the candidate with the most votes to the candidate with the least votes;
*	Diana DeGette (272,892 votes - 73.8% total of votes),
*	Charles Casper Stockham (85,213 votes - 23.0% total of votes),
*	Raymon Anthony Doane (11,606 votes - 3.1% total of votes).

5. As a result of the analysis, the winner of the election was Diana DeGette. The total number of votes it received was 272,892 and the percentage of votes it received was calculated as 73.8%.

## Election - Audit Summary

1. The counties that need to be analyzed in the selection are as written below.
* Jefferson,
* Denver,
* Arapahoe.

2. When it is necessary to write the county results,
* Jefferson County received 10.5 percent of the total vote.
* Denver County received 82.8 percent of the total vote.
* Arapahoe county received 6.7 percent of the total votes.

3. The county with the highest voter turnout became Denver with 82.8 percent of the total votes. A total of 306,055 votes were cast in Denver County.

## Python Programming Summary

While doing this selection analysis, it was decided to use python as the programming language. Python programming language, advanced code structure and high reliability analysis helped us to get the results. In general, the requirements for this analysis are; the number of votes cast in the entire election, the number of votes cast by the districts, the number of votes received by the electorate, and the percentages of all these analyses. In addition, a code was written for the determination of the voters and districts that received the most votes in the analysis. However, it is also possible to do more advanced analysis in the Python programming language. For this, more advanced codes and analysis methods can be used. Using VS Code while performing the analysis made it fun to work with its colorful interface.

#### CSV File

CSV file means that the information about the votes is separated by commas. What we use for this analysis is the district where the votes are cast together with the information about the electorate and the candidate preferred by the electorate in the election_results.csv file. In fact, the information given is sufficient for this analysis. However, factors such as age, education information, salary range, and the sector of work have a very important place in the results of the election surveys and public opinion surveys, which vary according to the countries.

#### Suggestions

On the basis of this project, the only thing I can say is that the data is sufficient and perhaps more different demographic variables should be included in the analysis. Because, although socio-economic status of people is necessary in an election analysis, it may not be too curious, but the ages and education levels of people will give us the chance to see the big picture about the electorate.
