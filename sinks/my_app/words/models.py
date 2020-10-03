from django.db import models

from django_extensions.db.models import TimeStampedModel


class Word(TimeStampedModel):
    text = models.CharField(max_length=300)
    count = models.IntegerField()