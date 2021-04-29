## Code files
The following files are used to generate the CSV files in order to create HITs for the MTurkers
- `aggregation_module.py`: Appends previous story contributions from HIT results to a new CSV used to generate the HITs for the next iteration. Essentially, this file will look at the state of the master csv sheet and determine what has to go into the aggregation HIT.
It takes this into account and generates a csv file that will serve as the input to the aggregation HIT.
- `QCInput.py`: Creates CSV used to generate HITs to filter out unusable story lines written in the previous iteration. Essentially, this
file takes the output CSV file of the aggregation HIT from MTurk and wrangles the data into the form of a csv file that will serve as the
input file to the quality control HIT in MTurk.
- `QCOutput.py`: Creates CSV used to generate HITs for the next iteration of the story. This file will take the output of the quality 
control HIT in MTurk and update the master sheet accordingly based on the results from the quality control HITs. In our quality control,
we will be assessing whether the proposed story extension makes sense and if the extension is interesting. For quality control measures,
we will have 2 negative quality controls and 1 positive quality control, to avoid the case where a turker blindly answers either yes or no.
The rating of interest will be on a scale of 1-5 and will be crucial in breaking ties between diverging storylines. 

## Analysis
We plan to analyze the feasibility of having MTurkers come up with comprehensible storylines that continues from previously crowdsourced stories. We may do some analysis that evaluates the quality and creativity of the writings as well. We will do this by examining the results from our quality control modules.
