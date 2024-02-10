#!/usr/bin/env python3

import json
import os

# define directory of current script
script_dir = os.path.dirname(__file__)

IsMainApp = (__name__ == "__main__")

def main(exercise_type):
    list_of_exercises = exercise_list(exercise_type)
    for i in range(len(list_of_exercises)):
        print(list_of_exercises[i].get('name'))

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

if IsMainApp:
    import argparse
    argparser = argparse.ArgumentParser(description='list of exercises of the specified type')
    argparser.add_argument('--ExerciseType',
                            required=True,
                            type=str)
    args = argparser.parse_args()
    main(args.ExerciseType)