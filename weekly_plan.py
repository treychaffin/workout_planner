#!/usr/bin/env python3

from workout_plan import workout_plan
from exercise_list import exercise_list

IsMainApp = (__name__ == "__main__")

def main(exercises_per_workout, plan):
    weekly_plan(exercises_per_workout, plan)

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

if IsMainApp:
    import argparse
    argparser = argparse.ArgumentParser(description='creates a weekly workout plan')
    argparser.add_argument('--ExercisesPerWorkout',
                        required=False,
                        default=4,
                        type=int)
    plan_list = []
    argparser.add_argument('--Plan',
                        required=False,
                        type=str,
                        action='append',
                        dest='plan_list')
    args = argparser.parse_args()
    if args.plan_list is None:
        args.plan_list = ['push','pull','legs']
    main(exercises_per_workout = args.ExercisesPerWorkout,
        plan = args.plan_list)