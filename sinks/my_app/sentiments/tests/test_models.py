from django.test import TestCase

from ..models import Tweet


class TestTweet(TestCase):
    def test_it_should_have_defined_fields(self):
        Tweet.objects.create(
            text='This is my first tweet!',
            search_term='first tweet',
            sentiment='positive'
        )

        tweet = Tweet.objects.last()

        self.assertEqual(tweet.text, 'This is my first tweet!')
        self.assertEqual(tweet.search_term, 'first tweet')
        self.assertEqual(tweet.sentiment, 'positive')
        self.assertIsNotNone(tweet.created)
        self.assertIsNotNone(tweet.modified)

    def test_sentiment_field_should_set_choices(self):
        expected = (
            ('positive', 'Positive'),
            ('neutral', 'Neutral'),
            ('negative', 'Negative'),
        )
        self.assertEqual(Tweet.sentiment.field.choices, expected)