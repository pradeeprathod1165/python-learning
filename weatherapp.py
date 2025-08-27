import requests

# --- SETTINGS ---
api_key = "08722ea037ad1d34285fbd619ddef9d3"  # Use your own API key

city = input("Enter city name: ")

# --- API URL ---
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# --- FETCH DATA ---
try:
	response = requests.get(url)
	response.raise_for_status()
	data = response.json()
	if data.get("cod") != 200:
		print(f"Error: {data.get('message', 'Unable to fetch weather data.')}")
	else:
		print("City:", data["name"])
		print("Temperature:", data["main"]["temp"], "°C")
		print("Humidity:", data["main"]["humidity"], "%")
		print("Weather:", data["weather"][0]["description"])
except requests.RequestException as e:
	print("Network error:", e)