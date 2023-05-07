import requests
from pandas import json_normalize
import json
import os

env = Env()
env.read_env()

proxy = env.str("PROXY")

os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy


with open('strava_tokens.json') as json_file:
    strava_tokens = json.load(json_file)  # Loop through all activities
url = "https://www.strava.com/api/v3/activities"
access_token = strava_tokens['access_token']  # Get first page of activities from Strava with all fields
r = requests.get(url + '?access_token=' + access_token)
r = r.json()

df = json_normalize(r)
df.to_csv('strava_activities_all_fields.csv')