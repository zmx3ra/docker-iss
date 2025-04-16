import requests
import json
import datetime
import logging
import os
from pymongo import MongoClient

# logging config
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_iss_location():
    url = "http://api.open-notify.org/iss-now.json"
    try:
        response = requests.get(url)
        r = response.json()

        # fetch values from response
        timestamp = r['timestamp']
        # convert timestamp to human readable date and time (out of epoch)
        dt_obj = datetime.datetime.fromtimestamp(timestamp)
        dtime = dt_obj.strftime('%Y-%m-%d-%H:%M:%S')

        # get longitude and latitude
        long = r['iss_position']['longitude']
        lat = r['iss_position']['latitude']

        # log output for visibility
        logger.info("Timestamp: " + dtime)
        logger.info("Longitude: " + long)
        logger.info("Latitude: " + lat)

        # write output to mongo db
        write_to_mongo(dtime, long, lat)

    except Exception as e:
        logger.error(e)
        exit(1)

def write_to_mongo(dtime, long, lat):
    # write output to mongo db
    try:
        # use an ENV variable for the password
        dbpass = os.getenv('MONGOPASS')
        if not dbpass:
            raise ValueError("MONGOPASS environment variable is not set")
            logging.error("MONGOPASS environment variable is not set")
            exit(1)
            
        connection_string = f'mongodb+srv://docker:{dbpass}@cluster0.m3fek.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
        client = MongoClient(connection_string)
        db = client['iss_location']
        collection = db['locations']
        collection.insert_one({'timestamp': dtime, 'longitude': long, 'latitude': lat})
        logger.info('Output written to MongoDB')
    except Exception as e:
        logger.error(e)
        exit(1)

if __name__ == "__main__":
    get_iss_location()
