# tracker.py
# Main file for Fitness Nutrition Tracker

from user_data import user_data, save_data, load_data
from utils import calculate_bmi

def log_workout(workout_type, duration_minutes):
    entry = {"type": workout_type, "duration": duration_minutes}
    user_data["workouts"].append(entry)
    print(f"Workout logged: {workout_type} for {duration_minutes} minutes.")

def log_meal(meal_name, calories):
    entry = {"meal": meal_name, "calories": calories}
    user_data["meals"].append(entry)
    print(f"Meal logged: {meal_name} with {calories} calories.")

def show_summary():
    print("\n Summary of Logged Data:")
    print("Workouts:")
    for w in user_data["workouts"]:
        print(f"  - {w['type']} for {w['duration']} minutes")
    print("Meals:")
    for m in user_data["meals"]:
        print(f"  - {m['meal']} with {m['calories']} calories")

if __name__ == "__main__":
    load_data()
    print("Welcome to Fitness Nutrition Tracker\n")

    log_workout("Running", 30)
    log_meal("Chicken Salad", 450)

    log_workout("Yoga", 60)
    log_meal("Oatmeal", 300)

    bmi = calculate_bmi(70, 1.75)
    print(f"\n Calculated BMI: {bmi:.2f}")

    show_summary()
    save_data()
