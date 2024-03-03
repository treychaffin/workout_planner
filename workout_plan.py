#!/usr/bin/env python3

import random
from exercise_list import exercise_list

IsMainApp = (__name__ == "__main__")

def main(exercise_type, exercises_per_workout):
    plan = workout_plan(exercise_list(exercise_type), exercises_per_workout)
    for i in range(len(plan)): print(plan[i])

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

    if exercises_per_workout > len(list_of_exercises):

        exercise_list.append(list_of_exercises)

        while (exercises_per_workout % len(exercise_list)) > exercises_per_workout:
            exercise_list.append(list_of_exercises)
            print(exercise_list)

        
        exercise_index = random.sample(list_of_exercises,(exercises_per_workout - len(exercise_list))) 
        for i in range(exercises_per_workout):
            exercise_list.append(list_of_exercises[exercise_index[i]].get('name'))
    else:
        exercise_index = random.sample(range(len(list_of_exercises)),
                                    exercises_per_workout)
        for i in range(exercises_per_workout):
            exercise_list.append(list_of_exercises[exercise_index[i]].get('name'))
    
    return exercise_list

# if IsMainApp:
#     import argparse
#     argparser = argparse.ArgumentParser(description='creates a workout plan from a list of exercises')
#     argparser.add_argument('--ExerciseType',
#                         required=True,
#                         type=str)
#     argparser.add_argument('--ExercisesPerWorkout',
#                         required=True,
#                         type=int)
#     args = argparser.parse_args()
#     main(args.ExerciseType,args.ExercisesPerWorkout)

print(workout_plan(exercise_list('legs'),8))