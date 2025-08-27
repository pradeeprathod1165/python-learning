import requests

# --- SETTINGS ---
city = "London"  
api_key = "08722ea037ad1d34285fbd619ddef9d3"  


# --- API URL ---
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
