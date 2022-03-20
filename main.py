# import request module
import requests

# import datetime class
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 165
AGE = 20

app_ID = "app_ID"
app_Key = "app_Key"

query = input("Tell me which exercises you did:  ")

headers = {
    "x-app-id": app_ID,
    "x-app-key": app_Key,
}

user_params = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=exercise_endpoint, json=user_params, headers=headers)
data = response.json()

sheet_endpoint = "https://api.sheety.co/4a68b9ed0b3df64a8831638ce3ec4a68/myWorkouts/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    data_sheet = {
        "workout": {
            "date": today_date,
            "time": "           " + now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_header = {
    "Authorization": "Basic_Autho"
}

sheet_response = requests.post(url=sheet_endpoint, json=data_sheet, headers=sheet_header)
print(sheet_response.text)
