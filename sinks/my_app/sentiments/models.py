from django.db import models

from django_extensions.db.models import TimeStampedModel


class Tweet(TimeStampedModel):
    text = models.TextField()
    search_term = models.CharField(max_length=300)

    SENTIMENT_CHOICES = (
        ('positive', 'Positive'),
        ('neutral', 'Neutral'),
        ('negative', 'Negative'),
    )
    sentiment = models.CharField(
        max_length=10,
        choices=SENTIMENT_CHOICES,
        default='neutral',
    )