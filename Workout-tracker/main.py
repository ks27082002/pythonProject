import requests
APP_ID = "c28db140"
API_KEY = "50be04176d5f3b25658222221ff1b241"
BEARER_TOKEN = "Bearer qwerty "
from datetime import  date
import time
# import os
# os.environ["APP_ID"] = APP_ID
# os.environ["API_KEY"] = API_KEY
# os.environ["BEARER_TOKEN"] = BEARER_TOKEN

API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/8733df2434363dff6967d520106ad4a2/myWorkoutsTracker/workouts"
header = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
query = input("Exercise u did ")
body = {
    "query": query
}

response = requests.post(url=API_ENDPOINT, headers=header, json=body)
print(response.json())

exe_data = [{"Exercise": item["user_input"], "Duration":item["duration_min"], "Calories": item['nf_calories']} for item in response.json()["exercises"]]

header2 = {
    "Content-Type": "application/json",
    "Authorization": BEARER_TOKEN
}
curr_date = date.today()
curr_date = curr_date.strftime("%d/%m/%Y")
curr_time = time.strftime( "%H:%M:%S", time.localtime())
for exe in exe_data:

    body2 = {
        "workout": {
            "date": curr_date,
            "time": curr_time,
            "exercise": exe["Exercise"].title(),
            "duration": exe["Duration"],
            "calories": exe["Calories"]

        }
    }
    response2 = requests.post(url=SHEETY_ENDPOINT, json=body2, headers=header2)
    print(response2.status_code)


