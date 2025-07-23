import json
import os
from datetime import datetime

DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"user": {}, "workouts": [], "meals": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_user_info(data):
    if not data["user"]:
        print("Welcome! Let's get you set up.")
        name = input("What's your name? ")
        height = float(input("Height in meters (e.g. 1.75): "))
        weight = float(input("Weight in kg (e.g. 75): "))
        bmi = round(weight / (height ** 2), 2)
        data["user"] = {"name": name, "height": height, "weight": weight, "bmi": bmi}
        save_data(data)
    return data["user"]

def log_workout(data):
    workout = input("Enter workout (e.g. Running): ")
    duration = int(input("Duration in minutes: "))
    data["workouts"].append({"activity": workout, "duration": duration})
    print(f"Workout logged: {workout} for {duration} minutes.")
    save_data(data)

def log_meal(data):
    meal = input("Enter meal name (e.g. Chicken Salad): ")
    calories = int(input("Enter calories: "))
    data["meals"].append({"meal": meal, "calories": calories})
    print(f"Meal logged: {meal} with {calories} calories.")
    save_data(data)

def view_summary(data):
    print("\n🔹 Summary of Logged Data 🔹")
    print("Workouts:")
    total_minutes = 0
    for w in data["workouts"]:
        print(f" - {w['activity']} for {w['duration']} minutes")
        total_minutes += w['duration']

    print("Meals:")
    total_calories = 0
    for m in data["meals"]:
        print(f" - {m['meal']} with {m['calories']} calories")
        total_calories += m['calories']

    print(f"\nTotal workout time: {total_minutes} minutes")
    print(f"Total calories eaten: {total_calories} calories")
    print(f"Your BMI: {data['user']['bmi']}\n")

def main():
    data = load_data()
    user = get_user_info(data)

    print(f"\n👋 Hello {user['name']}! Today is {datetime.now().strftime('%A, %B %d, %Y – %I:%M %p')}")

    while True:
        print("\nWhat would you like to do?")
        print("1. Log a workout")
        print("2. Log a meal")
        print("3. View summary")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            log_workout(data)
        elif choice == "2":
            log_meal(data)
        elif choice == "3":
            view_summary(data)
        elif choice == "4":
            print("Goodbye! Your data has been saved.\n")
            break
        else:
            print("Invalid choice. Please select 1–4.")

if __name__ == "__main__":
    main()
