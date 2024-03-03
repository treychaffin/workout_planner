from workout_plan import workout_plan
from exercise_list import exercise_list
import random

weekly_plan = {
    'exerciseSchedule' : ['push','legs','pull','legs'],
    'exercisesPerWorkout' : 4
}

exercise_schedule = weekly_plan.get('exerciseSchedule')
exercises_per_workout = weekly_plan.get('exercisesPerWorkout')

push_exercise_quantity = exercise_schedule.count('push')*exercises_per_workout
pull_exercise_quantity = exercise_schedule.count('pull')*exercises_per_workout
legs_exercise_quantity = exercise_schedule.count('legs')*exercises_per_workout

push_exercise_list = workout_plan(exercise_list('push'),push_exercise_quantity)
pull_exercise_list = workout_plan(exercise_list('pull'),pull_exercise_quantity)
legs_exercise_list = workout_plan(exercise_list('legs'),legs_exercise_quantity)

print(push_exercise_list)
print(pull_exercise_list)
print(legs_exercise_list)



def split_randomly_sample(data, num_pieces):
  """
  Splits a list into a specified number of randomly ordered pieces using sampling.

  Args:
      data: The list to split.
      num_pieces: The number of pieces to split the list into.

  Returns:
      A list of lists, where each sublist contains a portion of the original data.
  """
  sublists = []
  for _ in range(num_pieces):
    sublist = random.sample(data, k=len(data) // num_pieces)
    data = [item for item in data if item not in sublist]
    sublists.append(sublist)
  return sublists

for i in range(len(exercise_schedule)):
    if exercise_schedule[i] == 'push':
        print('push')
        
    if exercise_schedule[i] == 'pull':
        print('pull')
    if exercise_schedule[i] == 'legs':
        print('legs')
