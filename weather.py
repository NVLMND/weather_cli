
import datetime
import requests
import json
import os

def get_weather(CITY):
    #Enjoy key-
    api_key="e9b1e0a9122741289e675330251305"
    base_url="http://api.weatherapi.com/v1"
    forecast_url=f"{base_url}/forecast.json?q={CITY}&key={api_key}"

    response=requests.get(forecast_url, timeout=5)
    return response

def get_current(response):
    if response.status_code==200:
        data=response.json()
        updated=data["current"]["last_updated"]
        city=data["location"]["name"]
        country=data["location"]["country"]
        temp=data["current"]["temp_c"]
        wind=data["current"]["wind_kph"]
        hum=data["current"]["humidity"]
        condition=data["current"]["condition"]["text"]
        return updated, city, country, temp, wind, hum, condition
    else:
        return None

def get_forecast(response):
    if response.status_code==200:
        data=response.json()
        forecast_day=data["forecast"]["forecastday"][0]
        date=forecast_day["date"]
        maxtemp=forecast_day["day"]["maxtemp_c"]
        avgtemp=forecast_day["day"]["avgtemp_c"]
        mintemp=forecast_day["day"]["mintemp_c"]
        maxwind=forecast_day["day"]["maxwind_kph"]
        rain=forecast_day["day"]["daily_chance_of_rain"]
        snow=forecast_day["day"]["daily_chance_of_snow"]
        condition=forecast_day["day"]["condition"]["text"]
        return date, maxtemp, avgtemp, mintemp, maxwind, rain, snow, condition
    else:
        return None

def display_current(CITY):
    raw_data=get_weather(CITY)
    if raw_data:
        current_data=get_current(raw_data)
        if current_data:
            updated, city, country, temp, wind, hum, condition=current_data
            print(".\n.\n.")
            print(f"Last Updated: {updated}")
            print(f"City: {city}")
            print(f"Country: {country}")
            print(f"Temperature: {temp}°C")
            print(f"wind: {wind}kph")
            print(f"humidity: {hum}")
            print(f"Condition: {condition}\n.\n.\n")
            return {
                "updated": updated,
                "city": city,
                "country": country,
                "temperature": temp,
                "wind": wind,
                "humidity": hum,
                "condition": condition,
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    else:
        print("city not found.")
        return None

def display_forecast(CITY):
    raw_data=get_weather(CITY)
    if raw_data:
        forecast_data=get_forecast(raw_data)
        if forecast_data:
            date, maxtemp, avgtemp, mintemp, maxwind, rain, snow, condition=forecast_data
            print(".\n.\n.")
            print(f"Date: {date}")
            print(f"Max Temperature: {maxtemp}°C")
            print(f"Avg Temperature: {avgtemp}°C")
            print(f"Min Temperature: {mintemp}°C")
            print(f"Max Wind: {maxwind}kph")
            print(f"Rain: {rain}%")
            print(f"snow: {snow}%")
            print(f"Condition: {condition}\n.\n.\n.")
            return {
                "date": date,
                "maxtemperature": maxtemp,
                "avgtemperature": avgtemp,
                "mintemperature": mintemp,
                "maxwind": maxwind,
                "rain": rain,
                "snow": snow,
                "condition": condition,
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

    else:
        print("city not found.")
        return None

def main():
    file_path=os.path.join(os.path.dirname(__file__), "weather_history.json")
    if os.path.exists(file_path):
        with open(file_path, "r")as file:
            try:
                history=json.load(file)
            except json.JSONDecodeError:
                history=[]
    else:
        history=[]
    while True:
        CITY=input("Enter the city name to get the weather(or type 'exit' to quit): ").lower()
        if CITY=="exit":
            break
        raw_data=get_weather(CITY)
        if raw_data.status_code!=200:
            print("Invalid city name, try again.\n")
            continue
        while True:
            try:
                which_weather=int(input(".\n.\n.\nType-\nFor current weather '1'\nFor Forecast '2'\n: "))
                if which_weather==1:
                    history_record=display_current(CITY)
                    if history_record:
                        history.append(history_record)
                        with open(file_path, "w")as file:
                            json.dump(history, file, indent=4)
                        print("History Saved.")
                        break
                elif which_weather==2:
                    history_record=display_forecast(CITY)
                    if history_record:
                        history.append(history_record)
                        with open(file_path, "w")as file:
                            json.dump(history, file, indent=4)
                        print("History saved.")
                        break
                else:
                    print("choose between 1 or 2.")

            except ValueError:
                    print("Invalid Input.")

if __name__=="__main__":
    main()
