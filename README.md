# Python Push Pull Legs Workout Planner

This project is intended to create an easy way for me to make push, pull, legs
workout plans.

Exercises are stored as JSON files in the 'exercises' folder.

## creating an exercise

To create an exercise, run the 'create_exercise' function from the 
'create_exercise.py' file. 

Example:

    create_exercise('bench press','push')

The example shown will create an exercise with the name being 'Bench Press'
and the type being classified as a 'push' exercise. 

## creating a workout plan

To create a workout plan, run the 'create_plan' function from the 
'create_plan.py' file. 

Example:

    create_plan(4)

Output:

    *** push ***
    Dip
    Standing Overhead Press
    Decline Barbell Bench Press
    Barbell Flat Bench Press
    
    *** pull ***
    Barbell Shoulder Shrugs
    Chin-Up
    Deadlift
    Dumbell Hammer Curls
    
    *** legs ***
    Tib Bar Raises
    Barbell Front Squat
    Barbell Lunges
    Barbell Standing Calf Raises

The example shown will create an exercise plan with 4 exercises per workout.
