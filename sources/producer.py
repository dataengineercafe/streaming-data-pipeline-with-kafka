import json
import os

import tweepy
from confluent_kafka import Producer


CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')


topic = 'test-topic'

# Doc: docs.confluent.io/current/clients/confluent-kafka-python/
p = Producer({
    'bootstrap.servers': 'localhost:9092'
})

track = ['python',]


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status._json)
        print('---')
        p.produce(topic, json.dumps(status._json))
        p.flush()


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(
    auth=api.auth,
    listener=myStreamListener
)

myStream.filter(track=track)
