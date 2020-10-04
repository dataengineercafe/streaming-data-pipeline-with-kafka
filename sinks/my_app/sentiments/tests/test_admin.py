from django.contrib import admin
from django.test import TestCase

from ..admin import TweetAdmin
from ..models import Tweet


class TestTweetAdmin(TestCase):
    def test_admin_should_be_registered(self):
        self.assertTrue(isinstance(admin.site._registry[Tweet], TweetAdmin))

    def test_admin_should_set_list_display(self):
        expected = (
            'text',
            'search_term',
            'sentiment',
            'created',
            'modified',
        )
        self.assertEqual(TweetAdmin.list_display, expected)

    def test_admin_should_set_list_filter(self):
        expected = (
            'search_term',
            'sentiment',
        )
        self.assertEqual(TweetAdmin.list_filter, expected)

    def test_admin_should_set_search_fields(self):
        expected = (
            'text',
        )
        self.assertEqual(TweetAdmin.search_fields, expected)
