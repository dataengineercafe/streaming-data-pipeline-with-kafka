import json
import os
import re
import sys

import django

# Add the project to sys.path, so that Python can find packages
PROJECT_ROOT = os.path.join(os.path.dirname(__file__), 'my_app')
sys.path.append(PROJECT_ROOT)

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


# Credit: https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/calculate-tweet-word-frequencies-in-python/
def remove_url(txt):
    """Replace URLs found in a text string with nothing
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : string
        A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with url's removed.
    """

    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())


from confluent_kafka import Consumer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from words.models import Word


topics = ['test-topic',]

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest',
})

c.subscribe(topics)

while True:
    msg = c.poll(1.0)
    if msg is None:
        continue

    data = json.loads(msg.value().decode('utf-8'))
    text = data['text']
    print(text)

    word_tokens = set(remove_url(text).lower().split())
    stop_words = set(stopwords.words('english'))
    filtered_words = [w for w in word_tokens if not w in stop_words]
    for each in filtered_words:
        try:
            w = Word.objects.get(text=each)
            w.count = w.count + 1
            w.save()
        except Word.DoesNotExist:
            Word.objects.create(text=each, count=1)

    # total_words = Word.objects.count()
    # print('Total words:', total_words)

c.close()
