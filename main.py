import requests
from twilio.rest import Client

account_sid = "AC5682c9cbaa6c11f32402f92d38ebf8e6"
auth_token = "69980f5fbdf5f048e7b9361e0356417c"


weather_api = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "76a920fe5faf8326058744f7bc86b511"
paraameters = {
    "lat": 31.520370, # RESPECTED LOCATION LATITUDE
    "lon": 74.358749, # RESPECTED LOCATION LONGITUDE
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(weather_api,
                        params=paraameters
                        )
response.raise_for_status()
data = response.json()

will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    # print("bring an umbrella.")
    # if data["list"][0]["weather"][0]["id"] < 700:
    #     print("bring an umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="bring an umbrella.✌",
                        from_="+18329253283",
                        to="+917075912537"#YOUR PHONE NUMBER

                        )

    print(message.status)

