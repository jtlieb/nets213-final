'''
QCInput module that takes the output of the Aggregation HIT to form the
input to the Quality Control HIT. 
'''

import random
import csv
import pandas as pd

iteration = 1

INPUT_FILE = 'data/level1/batch_results_1.csv'
OUTPUT_FILE = 'data/QC_inputs/QC_HIT_INPUT.csv'

neg_qual_controls = [
    'dog dog went the to beach square computer',
    'open wall the saturday over restaurant the',
    'apples fall over between over sock',
    'circle round square corner side baseball cap',
    'blacksmith tuesday tree under the tent'
]

pos_qual_control = 'if you are reading this answer "Yes"'

'''
creates the input for the quality control HIT. 
must pass in the output csv dataframe of the aggregation HIT output.
'''
def create_input(mturk_res):

    story_dict = {}

    for i, row in mturk_res.iterrows():
        ref_story_id = row['Input.Referring_Story_Id']
        ref_decision_id = row['Input.Referring_Decision_Id']
        story = row['Input.Story']
        hit_id = row['HITId']
        worker_id = row['WorkerId']
        answer_story = row['Answer.Story']
        decision_1 = row['Answer.Decision1']
        decision_2 = row['Answer.Decision2']

        answer_story += '\nOption 1: ' + decision_1 + '\nOption 2: ' + decision_2

        key = str(ref_story_id) + "@" + str(ref_decision_id) + "@" + story

        if not key in story_dict:
            story_dict[key] = []

        story_dict[key].append(tuple([hit_id, answer_story]))
    

    res = []

    for key in story_dict:
        row = []

        elems = key.split("@")

        row.append(elems[0])
        row.append(elems[1])
        row.append(elems[2])

        input_ids = []
        inputs = []

        for i in story_dict[key]:
            input_ids.append(i[0])
            inputs.append(i[1])

        for i in input_ids:
            row.append(i)

        for i in inputs:
            row.append(i)

        row.append(pos_qual_control)
        row.append(random.choice(neg_qual_controls))
        row.append(random.choice(neg_qual_controls))

        res.append(row)

    
    return res


def main():
    # Read in CVS result file with pandas
    # PLEASE DO NOT CHANGE
    mturk_res = pd.read_csv(INPUT_FILE)

    # Call functions and output required CSV files

    with open(OUTPUT_FILE, mode='w') as csv_file:
        fieldnames = [
            'Referring_Story_Id',
            'Referring_Decision',
            'Story',
            'Input_1_Id',
            'Input_2_Id',
            'Input_3_Id',
            'Input_4_Id',
            'Input_1',
            'Input_2',
            'Input_3',
            'Input_4',
            'pos_qual',
            'neg_qual_1',
            'neg_qual_2'
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for tup in create_input(mturk_res):
            print(len(tup), "should be 14")
            writer.writerow({
                'Referring_Story_Id': tup[0],
                'Referring_Decision': tup[1],
                'Story': tup[2],
                'Input_1_Id': tup[3],
                'Input_2_Id': tup[4],
                'Input_3_Id': tup[5],
                'Input_4_Id': tup[6],
                'Input_1': tup[7],
                'Input_2': tup[8],
                'Input_3': tup[9],
                'Input_4': tup[10],
                'pos_qual': tup[11],
                'neg_qual_1': tup[12],
                'neg_qual_2': tup[13]
            })

    # master_data = pd.read_csv(f"MASTER_{iteration - 1}.csv")
    # qc_data = pd.read_csv('QC_MODULE_OUTPUT.csv')

    # story_cons = dict()  # (ref_story, ref_decision) -> (HitId, input, decision1, decision2)

    # for i, row in qc_data.iterrows():
    #     ref_story = row["Referring_Story_Id"]
    #     ref_dec = int(row["Referring_Decision"])
    #     hit_id = row["HitId"]
    #     input = row["Input"]
    #     dec_1 = row["Decision_1"]
    #     dec_2 = row["Decision_2"]

    #     story_cons[(ref_story, ref_dec)] = (hit_id, input, dec_1, dec_2)

    # # Add new data to master_data dataframe
    # for (ref_story, ref_dec), (hit_id, input, dec_1, dec_2) in story_cons.items():
    #     df = pd.DataFrame({"HitId": [hit_id],
    #                        "Text": [input],
    #                        "Decision1": [dec_1],
    #                        "Decision2": [dec_2],
    #                        "Referring_Story_Id": [ref_story],
    #                        "Referring_Decision": [ref_dec]
    #                        })

    #     master_data = master_data.append(df, ignore_index=True)

    # master_data.to_csv(f'MASTER_{iteration}.csv', index=False)


if __name__ == '__main__':
    main()
