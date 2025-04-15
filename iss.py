import requests
import json
import datetime

url = "http://api.open-notify.org/iss-now.json"

try:
    response = requests.get(url)
    r = response.json()

    # fetch values from response
    timestamp = r['timestamp']
    # convert timestamp to human readable date and time (out of epoch)
    datetime = datetime.datetime.fromtimestamp(timestamp)
    dtime = datetime.strftime('%Y-%m-%d-%H:%M:%S')

    # get longitude and latitude
    long = r['iss_position']['longitude']
    lat = r['iss_position']['latitude']

    # print output to console
    print(dtime)
    print(long)
    print(lat)

except Exception as e:
    print(e)
    exit(1)

# write output to file. Could also be to external database or other system.
try:
    lines = [dtime, "\n", long, "\n", lat]
    with open('/data/output.txt', 'w') as f:
        f.writelines(lines)
except Exception as e:
    print(e)
    exit(1)