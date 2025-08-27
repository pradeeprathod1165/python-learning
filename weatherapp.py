import requests

# --- SETTINGS ---
city = "London"  
api_key = "08722ea037ad1d34285fbd619ddef9d3"  


# --- API URL ---
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# --- FETCH DATA ---
response = requests.get(url)
data = response.json()

# --- DISPLAY DATA ---
print("City:", data["name"])
print("Temperature:", data["main"]["temp"], "°C")
print("Humidity:", data["main"]["humidity"], "%")
print("Weather:", data["weather"][0]["description"])