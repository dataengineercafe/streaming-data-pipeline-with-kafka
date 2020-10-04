import os
import sys

import django

# from confluent_kafka import Consumer
#
#
# c = Consumer({
#     'bootstrap.servers': 'localhost:9092',
#     'group.id': 'mygroup',
# })
#
# c.subscribe(['mytopic'])

# Add the project to sys.path, so that Python can find packages
PROJECT_ROOT = os.path.join(os.path.dirname(__file__), 'my_app')
sys.path.append(PROJECT_ROOT)

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


from words.models import Word


# while True:
#     msg = c.poll(1.0)
#     if msg is None:
#         continue

    # print(f'Received message: {msg.value().decode("utf-8")}')

text = 'song'

try:
    w = Word.objects.get(text=text)
    w.count = w.count + 1
    w.save()
except Word.DoesNotExist:
    Word.objects.create(text=text, count=1)

total_words = Word.objects.count()
print('Total words:', total_words)

# c.close()
