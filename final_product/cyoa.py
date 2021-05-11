# -*- coding: utf-8 -*-
"""CYOA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1721ufg5PDWB9UZQ5QqsmWXNihG3qDd77
"""

import csv
import pandas as pd
import time
import random

MAX_DEPTH = 6


class StoryLevel:

    def __init__(self, row):
        self.id = row["HitId"]
        self.text = row["Text"]
        self.d1 = row["Decision1"]
        self.d2 = row["Decision2"]
        self.d1_next_id = row["Decision1_HitId"]
        self.d2_next_id = row["Decision2_HitId"]


def dot_dot_dot():
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)


def random_chars():
    options = ['%', '&', '#', '*', "<", ">", "/", "\\", "|", "@"]
    time.sleep(1)
    for i in range(5):
        print("".join([random.choice(options) for i in range(100)]))
        time.sleep(0.2)


# START GAME
def main():

    # DEFINE STORY TREE AND LOAD IN DATA
    story_tree = dict()

    master_data = pd.read_csv(
        "/Users/justinlieb/Documents/College/Spring 2021/NETS 213/nets213-final/data/level6/MASTER_6.csv")

    for i, row in master_data.iterrows():
        level = StoryLevel(row)
        story_tree[level.id] = level

    print("Are you ready to start your quest? Type \"I am ready to test my will and determination!!!\" if you are prepared.")
    res = input()
    dot_dot_dot()
    while not res == "I am ready to test my will and determination!!!":
        print("\nSeems like you don't have enough will or determination to complete this quest. Try again. \n\n")
        time.sleep(0.5)
        print(
            "Type \"I am ready to test my will and determination!!!\" if you are prepared.")
        res = input()
        dot_dot_dot()

    print("\nExcellent choice, young blacksmith! Let's begin!")

    # PRINT DIAMOND FOR DRAMA
    for i in range(20):
        count = 101
        stars = ["*" for x in range(1 + 4*i)]
        spaces = [" " for j in range(int((101 - (1 + 4*i)) / 2))]
        print("".join(spaces + stars + spaces))
        time.sleep(0.1)

    print("                         ONCE UPON A TIME(D HIT): THE TALE OF THE BLACKSMITH")

    for i in reversed(range(19)):
        count = 101
        stars = ["*" for x in range(1 + 4*i)]
        spaces = [" " for j in range(int((101 - (1 + 4*i)) / 2))]
        print("".join(spaces + stars + spaces))
        time.sleep(0.1)
    while True:
        cur_level = story_tree["ORIGINAL"]
        level = 1

        commentary = ["Hmmm, bold choice young lad.", "Ohhhhh, you shall come to regret this decision.",
                      "Interesting.", "Oh dear God, that is all I can say to that horrendous decision."]

        while True:
            print("\n\n**** LEVEL " + str(level) + "****\n")
            if level == 1:
                print("You are a blacksmith working for the royal forge. The commoners aren't happy with the monarch and you've secretly been making weapons for a potential uprising.")

            print(cur_level.text)
            print("\n")
            time.sleep(3)
            print("** OPTION 1: " + str(cur_level.d1) + " **")
            time.sleep(1)
            print("** OPTION 2: " + str(cur_level.d2) + " **")
            time.sleep(1)
            print("\n Type \"1\" or \"2\" to select your choice")
            response = None
            while True:
                response = int(input())
                if (response == 1 or response == 2):
                    break

                print("still here")
                print("\nTry again. Type \"1\" or \"2\" to select your choice")

            dot_dot_dot()
            print(random.choice(commentary) + "\n\n")
            random_chars()

            level += 1
            cur_level = story_tree[cur_level.d1_next_id if response ==
                                   1 else cur_level.d2_next_id]
            if level == MAX_DEPTH:
                break

        print("\n\n")
        random_chars()

        print("\n\n **** YOUR FATE: **** ")
        dot_dot_dot()
        print("\n\n")
        print(cur_level.text)
        print("\n\n")
        dot_dot_dot()
        print("Interesting. But you can do better. Try again? Say \"Yes\" to start, anything else to stop.")
        newline = input()
        if (newline != "Yes"):
            break


if __name__ == "__main__":
    main()