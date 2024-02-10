#!/usr/bin/env python3

import json
import os

IsMainApp = (__name__ == "__main__")

# define directory of current script
script_dir = os.path.dirname(__file__)

def main(exercise_name,exercise_type):
    create_exercise(exercise_name,exercise_type)

def create_exercise(exercise_name,exercise_type):
    '''

    Parameters
    ----------
    exercise_name : String
        Name of the exercise to create.
    exercise_type : String
        Type of the exercise; push, pull, legs.

    Returns
    -------
    None.

    '''
    
    ##########################################################################
    # process user input
    ##########################################################################
    
    # capitalize every first letter, lowercase every other letter
    exercise_name = exercise_name.title()
    
    # lowercase all letters
    exercise_type = exercise_type.lower()
    
    # ensure exercise type is either push, pull, or legs
    while not (exercise_type == "push" 
       or exercise_type == "pull" 
       or exercise_type == "legs"):
        print("Exercise Type must be; push, pull, or legs")
        exercise_type = input("Exercise Type (push, pull, legs): ").lower()
        
    # create exercise file name, 
    # lowercase letters, replace spaces with underscores
    exercise_filename = exercise_name.lower().replace(" ", "_")+".json"
    
    ########################################################################## 
    # create file path
    ########################################################################## 
    
    # define exercise folder name, prepend script directory
    exercise_foldername = os.path.join(script_dir,"exercises")
    
    # check if exercise folder exists, create the folder if not
    if(os.path.isdir(exercise_foldername) != True): 
        os.makedirs(exercise_foldername)
        print("exercise folder created")
        
    # define the path for the exercise JSON file
    exercise_filepath = os.path.join(exercise_foldername,exercise_filename)
    
    ##########################################################################
    # create JSON file
    ##########################################################################
    
    # create dictionary for exercise
    exercise = {
        "name": exercise_name,
        "type": exercise_type
    }
    
    # write exercise as JSON file
    with open(exercise_filepath,"w+") as file:
        file.write(json.dumps(exercise))
        
    # let user know file has been created
    print("*** Exercise Created ***")    
    print("Exercise Name: ",exercise_name)
    print("Exercise Type: ",exercise_type)
    print("Filename:      ",exercise_filename)
    print("Filepath:      ",exercise_filepath)
    print()

if IsMainApp:
    import argparse
    argparser = argparse.ArgumentParser(description='adds an json exercise to the exercises folder')
    argparser.add_argument('--ExerciseName',
                        required=True,
                        type=str)
    argparser.add_argument('--ExerciseType',
                        required=True,
                        type=str)
    args = argparser.parse_args()
    main(args.ExerciseName,args.ExerciseType)