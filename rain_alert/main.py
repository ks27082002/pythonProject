
from twilio.rest import Client
import requests

api_key = "51e9c14e19f326d9db30e6b4761d4475"
account_sid = 'ACf550b400ec77e3ee5d0eea84e945bcf3'
auth_token = '3b1896a7737309b846888bdf2e29ec04'


parameters = {
    "lat": 19.0760,
    "lon": 72.8777,
    "appid": api_key,
    "exclde" : "current,minutely,daily"

}



will_rain = False
response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
# print(response.json())
weather_data = response.json()
print(weather_data)
for hour_data in weather_data["weather"][0:2]:
    #print(hour_data)
    if hour_data["id"] < 700:
        will_rain = True

if will_rain:
    #print("HII")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain. Bring Umbrella☔",
        from_='+12343199779',
        to='+919175095845'
    )
    print(message.status)