# Once Upon a Time<sub>d HIT</sub>:
## A Crowdsourced Text Adventure Game
The main components of our game include:
1. Coming up with a general storyline 
2. Crowdsourcing locations as well as situations that could occur in those locations
3. Crowdsourcing the different paths the story could take
4. Compiling all the paths together and implementing the game

## Coming up with a general storyline - 1 pt
This should be pretty straightforward. We want to make the story
both interesting and general enough so that Turkers will be able
to expand on it in different directions.

Milestones:
- Come up with interesting, general storyline as a baseline for the game

## Crowdsourcing locations as well as situations that could occur in those locations - 2 pts
We intend on creating 100 initial HITs to generate locations and 
interesting situations that could occur in those locations,
given a general storyline of our creation. After these HITs
are completed, we will institute another round of HITs 
to verify the quality of the submitted inputs.

Milestones: 
- Create HTML for the 100 initial HITs
- Publish 100 HITs
- Create HTML for the quality control HITs
- Publish quality control HITs

## Crowdsourcing the different paths the story could take - 10 pts (1 pt per level in the game tree)
This component of the project will be executed in a level-by-level fashion, 
in terms of how far along the game tree we have gotten. We intend on 
adding 10 levels to the game tree, which means there would be 10 decisions 
to be made before the game ends. 

The first level will consist of 2 HITs where the Turkers are given an initial
storyline and a particular location and situation that will be randomly selected
from the results of the previous part. Their job is to first come up with a pair of
two contrasting actions the player/character can take in the given location and situation,
and then write a story block the story so far to those actions. After that,
we will publish a batch of some low and odd number of HITs to vote on which story
continuation submission is better, and branch off the story into two separate paths 
based on the pair of actions that were selected. 

Each level will therefore be exponentially larger than the last, and this above process will 
continue for each individual storyline node. Hence, each node will receive a new, unique location
and situation to connect the ongoing storyline to, and this process will continue until
each path has hit 10 nodes. 

Milestones:
- Create HTML for storyline continuation HITs
- Create HTML for quality control HITs for the storyline continuation submissions
- Publish 2 HITs per node
- Publish a low and odd number of HITs to determine the superior storyline continuation
- Repeat process for every node at each level

## Implementing the game - 4 pts
This will involve compiling all the .csv files that we have obtained through the HITs
on MTurk, and then implementing a game tree data structure via those results.

Additionally, we will need to write the logic for the game itself.

Milestones:
- Compile .csv results 
- Create game tree data structure, to be used for the game
- Develop game logic
- Play game
