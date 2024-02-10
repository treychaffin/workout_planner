# Python Push Pull Legs Workout Planner

This project is intended to create an easy way for me to make push, pull, legs
workout plans.

Exercises are stored as JSON files in the 'exercises' folder.

## creating an exercise

To create an exercise, run `create_exercise.py` using the flags `--ExerciseName`
and `--ExerciseType`.

Each exercise will be saved as a JSON file in the "exercises" folder. If the 
folder doesn't exist, it will be created automatically

Example:

    python3 create_exercise.py --ExerciseName "Barbell Bench Press" --ExerciseType push

The example shown will create an exercise with the name being 'Bench Press'
and the type being classified as a 'push' exercise. 

Output:

    *** Exercise Created ***
    Exercise Name:  Barbell Bench Press
    Exercise Type:  push
    Filename:       barbell_bench_press.json
    Filepath:       \\10.0.10.5\nas\projects\python-workout-planner\exercises\barbell_bench_press.json

## show list of available exercises by type

The `exercise_list.py` script will print a list of exercises in your exercises 
folder by type using the `--ExerciseType` flag.

Example:

    python3 exercise_list.py --ExerciseType legs

Output:

    Barbell Back Squat
    Barbell Front Squat
    Barbell Glute Bridge
    Barbell Good Mornings
    Barbell Lunges
    Barbell Standing Calf Raises
    Tib Bar Raises

## create a workout plan

The `workout_plan.py` script will print a workout plan. The script will randomly 
choose exercises of the specified type and specified amount. 

The flag `--ExerciseType` will define what type of exercises to use. 

The flag `--ExercisesPerWorkout` will define how many exercise to include in the 
workout.

Example:

    python3 workout_plan.py --ExerciseType legs --ExercisesPerWorkout 5

Output:

    Barbell Standing Calf Raises
    Barbell Lunges
    Barbell Good Mornings
    Barbell Back Squat
    Barbell Front Squat

## create a weekly plan

The `weekly_plan.py` will print out a weekly workout plan.

The `--ExercisesPerWorkout` flag will define how many exercises per workout. If 
the flag isn't called, the exercises per workout will default to 4. 

The `--Plan` flag can be used to define a custom weekly plan.

Example:

    python3 weekly_plan.py --ExercisesPerWorkout 3 --Plan push --Plan legs --Plan pull --Plan legs

Output:

    *** push ***
    Incline Dumbell Bench Press
    Barbell Flat Bench Press
    Seated Barbell Overhead Press

    *** legs ***
    Barbell Front Squat
    Barbell Standing Calf Raises
    Barbell Good Mornings

    *** pull ***
    Barbell Shoulder Shrugs
    Deadlift
    Wide Grip Pull-Up

    *** legs ***
    Barbell Glute Bridge
    Tib Bar Raises
    Barbell Standing Calf Raises