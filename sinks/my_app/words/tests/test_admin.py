from django.contrib import admin
from django.test import TestCase

from ..admin import WordAdmin
from ..models import Word


class TestWordAdmin(TestCase):
    def test_admin_should_be_registered(self):
        self.assertTrue(isinstance(admin.site._registry[Word], WordAdmin))

    def test_admin_should_set_list_display(self):
        expected = (
            'text',
            'count',
        )
        self.assertEqual(WordAdmin.list_display, expected)

    def test_admin_should_set_ordering(self):
        expected = (
            '-count',
        )
        self.assertEqual(WordAdmin.ordering, expected)

    def test_admin_should_set_search_fields(self):
        expected = (
            'text',
        )
        self.assertEqual(WordAdmin.search_fields, expected)
