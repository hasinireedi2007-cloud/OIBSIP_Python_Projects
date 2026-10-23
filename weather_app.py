import requests

API_KEY = "7332db7b88d76f669a8299825680d703"

city = input("Enter city name: ")

url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q={city}&appid={API_KEY}&units=metric"
)

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()

        print("\n===== WEATHER REPORT =====")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels Like:", data["main"]["feels_like"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])
        print("==========================")

    elif response.status_code == 401:
        print("Invalid API key or the key is not active yet.")

    elif response.status_code == 404:
        print("City not found. Please check the spelling.")

    else:
        print("Unable to fetch weather. Status:", response.status_code)

except requests.exceptions.RequestException:
    print("Network error. Please check your internet connection.")