# Added docstrings and comments for clarity
# tracker.py
# Main file for Fitness Nutrition Tracker

def log_workout(workout_type, duration_minutes):
    print(f"Workout logged: {workout_type} for {duration_minutes} minutes.")

def log_meal(meal_name, calories):
    print(f"Meal logged: {meal_name} with {calories} calories.")

if __name__ == "__main__":
    print("Welcome to Fitness Nutrition Tracker")
    log_workout("Running", 30)
    log_meal("Chicken Salad", 450)

log_workout("Yoga", 60)
log_meal("Oatmeal", 300)
