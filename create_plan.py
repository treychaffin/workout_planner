# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 20:39:12 2024

@author: Trey
"""

import json
import os
import random

# define directory of current script
script_dir = os.path.dirname(__file__)

# create workout
def create_plan(exercises_per_workout):
    '''
    This function creates and prints a push, pull, legs plan    

    Parameters
    ----------
    exercises_per_workout : integer
        The number of exercises per session

    Returns
    -------
    None.

    '''

    # define exercise folder name, prepend script directory
    exercise_foldername = os.path.join(script_dir,"exercises")

    # create list of exercises in exercises folder
    exercise_files = os.listdir(exercise_foldername)

    # create list for exercises to go in
    push_list = []
    pull_list = []
    legs_list = []

    # fill the list with exercises
    for i in range(len(exercise_files)):
        with open(os.path.join(exercise_foldername,exercise_files[i])) as file:
            exercise = json.load(file)
            if (exercise.get('type') == 'push'):
                push_list.append(exercise)
            elif (exercise.get('type') == 'pull'):
                pull_list.append(exercise)
            elif (exercise.get('type') == 'legs'):
                legs_list.append(exercise)
    
    # create empty lists, to be filled later
    push = []
    pull = []
    legs = []
    
    # create a list of random, non-repeating indexes from exercises list
    push_index = random.sample(range(len(push_list)),exercises_per_workout)
    pull_index = random.sample(range(len(pull_list)),exercises_per_workout)
    legs_index = random.sample(range(len(legs_list)),exercises_per_workout)

    # create list of non-repeating exercises
    for i in range(exercises_per_workout):
        push.append(push_list[push_index[i]].get('name'))
        pull.append(pull_list[pull_index[i]].get('name'))
        legs.append(legs_list[legs_index[i]].get('name'))
    
    # print plan
    print('*** push ***')
    for i in range(len(push)):
        print(push[i])
    print()
    print('*** pull ***')
    for i in range(len(pull)):
        print(pull[i])
    print()
    print('*** legs ***')
    for i in range(len(legs)):
        print(legs[i])
    