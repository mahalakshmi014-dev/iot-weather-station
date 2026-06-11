import requests
import random
import time

API_KEY = "V6YMYNKW8IGV0U0Q"
URL = "https://api.thingspeak.com/update"

print("IoT Weather Station Started...")
print("Sending data to ThingSpeak every 20 seconds")
print("Press Ctrl+C to stop\n")

for i in range(10):
    temperature = round(random.uniform(28.0, 38.0), 2)
    humidity = round(random.uniform(55.0, 85.0), 2)
    
    response = requests.get(URL, params={
        "api_key": API_KEY,
        "field1": temperature,
        "field2": humidity
    })
    
    print(f"Reading {i+1}: Temp={temperature}°C | Humidity={humidity}% | Response={response.status_code}")
    time.sleep(20)

print("\nDone! Check ThingSpeak for graphs.")
