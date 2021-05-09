# -*- coding: utf-8 -*-
"""AggregationModule 213 Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vPSdGegDgh44QfJKxSkP_RwwUWxlnuQ2
"""

import random
import csv
import pandas as pd
import math


def create_input(mturk_res):
  stories = []
  for i, row in mturk_res.iterrows():
      story_so_far = []
      decision_1 = row['Decision1_HitId']
      # print(decision_1)
      # Represent the data we need to store for each story:
      first = []
      sec = []
      first.append(row['HitId'])
      sec.append(row['HitId'])

      first.append(row['Decision1'])
      sec.append(row['Decision2'])
      # print(isinstance(decision_1, str))
      print(row)
      if isinstance(decision_1, str) or math.isnan(decision_1):
        curr_referring_story = row['Referring_Story_Id']
        story_so_far.append(row['Text'])
        referring_decision = row['Referring_Decision']
        branch1 = row['Decision1']
        branch2 = row['Decision2']
        while (isinstance(curr_referring_story, str) or not math.isnan(curr_referring_story)):
          for i2, row2 in mturk_res.iterrows():
            if row2['HitId'] == curr_referring_story:
              # story_so_far.append(referring_decision)
              referring_decision = row2['Referring_Decision']

              story_so_far.append(row2['Text'])
              curr_referring_story = row2['Referring_Story_Id']

        story_so_far.reverse()
        story1 = story_so_far.copy()
        story2 = story_so_far.copy()
        story1.append(branch1)
        story2.append(branch2)
        
        first.append(story1)
        sec.append(story2)
        stories.append(first)
        stories.append(sec)
        # print(stories)
  return stories

 
def main():
  mturk_res = pd.read_csv('../data/level3/MASTER_3.csv')
  res = create_input(mturk_res)
  with open('../data/level4/AGG_HIT_INPUT.csv', mode='w', newline='') as csv_file:
    fieldnames = [
              'Referring_Story_Id', 
              'Referring_Decision', 
              'Story',
          ]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for tup in res:
            print(tup)
            writer.writerow({
                'Referring_Story_Id' : tup[0], 
                'Referring_Decision' : tup[1], 
                'Story' : ' '.join(tup[2])
            })





if __name__ == '__main__':
    main()

