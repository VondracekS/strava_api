import requests
import json
import time  # Get the tokens from file to connect to Strava

from environs import Env
import os


env = Env()
env.read_env()

proxy = env.str("PROXY")

os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy


with open('strava_tokens.json') as json_file:
    strava_tokens = json.load(json_file)  # If access_token has expired then
# use the refresh_token to get the new access_token
if strava_tokens['expires_at'] < time.time():  # Make Strava auth API call with current refresh token
    response = requests.post(
        url='https://www.strava.com/oauth/token',
        data={
            'client_id': [env.int("CLIENT_ID")],
            'client_secret': [env.str("CLIENT_SECRET")],
            'code': [env.str("CODE_URL")],
            'grant_type': 'authorization_code'
        }
    )  # Save response as json in new variable
    new_strava_tokens = response.json()  # Save new tokens to file
    with open('strava_tokens.json', 'w') as outfile:
        json.dump(new_strava_tokens, outfile)  # Use new Strava tokens from now
    strava_tokens = new_strava_tokens  # Open the new JSON file and print the file contents

# Make Strava auth API call with your
# client_code, client_secret and code
# to check it's worked properly
with open('strava_tokens.json') as check:
    data = json.load(check)
print(data)
