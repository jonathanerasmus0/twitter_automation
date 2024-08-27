# tweet_status_once.py

import tweepy
import time
import logging
from config import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Setup logging
logging.basicConfig(
    filename='tweet_status_once.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def tweet_status():
    # The status to be posted
    status = "API working correctly"
    
    # Send a tweet
    try:
        api.update_status(status)
        logging.info(f"Tweeted successfully: {status}")
        print(f"Tweeted: {status}")
    except tweepy.errors.TweepyException as e:
        logging.error(f"Error while tweeting: {e}")
        print(f"Error: {e}")

# Wait until the specified time (7:30 PM)
target_time = "19:24"
current_time = time.strftime("%H:%M")

while current_time != target_time:
    print(f"Current time is {current_time}. Waiting for {target_time}.")
    time.sleep(30)  # Check every 30 seconds
    current_time = time.strftime("%H:%M")

# Once the time is reached, tweet the status
tweet_status()
