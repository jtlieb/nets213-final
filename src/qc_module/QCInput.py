import random
import csv
import pandas as pd

neg_qual_controls = [
    'dog dog went the to beach square computer',
    'open wall the saturday over restaurant the',
    'apples fall over between over sock',
    'circle round square corner side baseball cap',
    'blacksmith tuesday tree under the tent'
]

def create_input(mturk_res):

    story_dict = {}

    for i, row in mturk_res.iterrows():
        ref_story_id = row['Referring_Story_Id']
        ref_decision_id = row['Referring_Decision_Id']
        story = row['Story']
        hit_id = row['HitId']
        worker_id = row['WorkerId']
        answer_story = row['Answer.Story']

        key = tuple([ref_story_id, ref_decision_id, story])

        if not key in story_dict:
            story_dict[key] = []

        story_dict[key].append(tuple([hit_id, answer_story]))

    res = []

    for key in story_dict:
        row = []

        row.append(key[0])
        row.append(key[1])
        row.append(key[2])

        input_ids = []
        inputs = []

        for i in story_dict[key]:
            input_ids.append(i[0])
            inputs.append(i[1])

        for i in input_ids:
            row.append(i)

        for i in inputs:
            row.append(i)

        row.append(random.choice(neg_qual_controls))
        row.append(random.choice(neg_qual_controls))
        
        

    


def main():
    # Read in CVS result file with pandas
    # PLEASE DO NOT CHANGE
    mturk_res = pd.read_csv('AGG_HIT_OUTPUT.csv')

    # Call functions and output required CSV files

    with open('data/input/QC_HIT_INPUT.csv', mode='w') as csv_file:
        fieldnames = [
            'Referring_Story_id', 
            'Referring_Decision_Id', 
            'Story',
            'Input_1_Id',
            'Input_2_Id',
            'Input_3_Id',
            'Input_4_Id',
            'Input_1',
            'Input_2',
            'Input_3',
            'Input_4',
            'neg_qual_1',
            'neg_qual_2'
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()

        for tup in create_input(mturk_res):
            writer.writerow({
                'Referring_Story_id' : tup[0], 
                'Referring_Decision_Id' : tup[1], 
                'Story' : tup[2],
                'Input_1_Id' : tup[3],
                'Input_2_Id' : tup[4],
                'Input_3_Id' : tup[5],
                'Input_4_Id' : tup[6],
                'Input_1' : tup[7],
                'Input_2' : tup[8],
                'Input_3' : tup[9],
                'Input_4' : tup[10],
                'neg_qual_1' : tup[11],
                'neg_qual_2' : tup[12]
            })



if __name__ == '__main__':
    main()


