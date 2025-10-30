import requests
from datetime import datetime

url = "https://api.carbonintensity.org.uk/intensity"
r = requests.get(url)
data = r.json()["data"][0]["intensity"]

print(f"🕒 Time: {datetime.now().strftime('%H:%M:%S')}")
print(f"Forecast: {data['forecast']} gCO₂/kWh | Actual: {data['actual']} gCO₂/kWh | Status: {data['index']}")
