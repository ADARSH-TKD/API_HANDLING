import requests



url = "https://api.frankfurter.app/2025-05-15?from=USD&to=INR"
response = requests.get(url)
data = response.json()

rate = data["rates"]["INR"]
date = data["date"]
print(rate, date)