import requests
import json
import datetime

response = requests.get("http://api.open-notify.org/iss-now.json")

obj = response.json()

timestamp = obj['timestamp']

datetime = datetime.datetime.fromtimestamp(timestamp)
dtime = datetime.strftime("%m/%d/%Y-%H:%M:%S")
long = obj['iss_position']['longitude']
lat = obj['iss_position']['latitude']

print(dtime)
print(long)
print(lat)

lines = [dtime, "\n", long, "\n", lat]

with open("/data/output.txt", "w") as file:
    file.writelines(lines)
