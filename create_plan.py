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

def workout_plan(list_of_exercises, exercises_per_workout):
    '''
    randomly creates a list of workouts of the specified ammount.

    Parameters
    ----------
    list_of_exercises : list
        list of available exercises.
    exercises_per_workout : int
        the ammount of exercises per workout
    Returns
    -------
    exercise_list : list
        the workout plan

    '''
    
    exercise_list = []
    
    exercise_index = random.sample(range(len(list_of_exercises)),
                                   exercises_per_workout)
    for i in range(exercises_per_workout):
        exercise_list.append(list_of_exercises[exercise_index[i]].get('name'))
    
    return exercise_list

# create exercise list
def exercise_list(exercise_type):
    '''
    creates and returns a list of available exercises from the exercises
    subfolder that have the matching type

    Parameters
    ----------
    exercise_type : str
        Type of exercise; push, pull, legs.

    Returns
    -------
    exercise_list : list
        A list of available exercise with the corresponding type

    '''
    
    exercise_list = []
    
    # define exercise folder name, prepend script directory
    exercise_foldername = os.path.join(script_dir,"exercises")

    # create list of exercises in exercises folder
    exercise_files = os.listdir(exercise_foldername)
    
    for i in range(len(exercise_files)):
        with open(os.path.join(exercise_foldername,exercise_files[i])) as file:
            exercise = json.load(file)
            if (exercise.get('type') == exercise_type):
                exercise_list.append(exercise)
    
    return exercise_list

# create weekly workout plan
def weekly_plan(exercises_per_workout=4, plan=['push','pull','legs']):
    '''
    creates a weekly workout plan and prints the plan to console

    Parameters
    ----------
    exercises_per_workout : int
        The ammount of exercises per each workout. The default is 4.
    plan : list
        The workout type plan. The default is ['push','pull','legs'].

    Returns
    -------
    none.

    '''
    
    for i in range(len(plan)):
        session_plan = workout_plan(exercise_list(plan[i]), 
                                    exercises_per_workout)
        print(f'*** {plan[i]} ***')
        for i in range(len(session_plan)): print(session_plan[i]) 
        print()    