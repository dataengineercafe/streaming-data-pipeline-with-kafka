from django.test import TestCase

from ..models import Word


class TestWord(TestCase):
    def test_it_should_have_defined_fields(self):
        Word.objects.create(
            text='tweet',
            count=5
        )

        word = Word.objects.last()

        self.assertEqual(word.text, 'tweet')
        self.assertEqual(word.count, 5)
        self.assertIsNotNone(word.created)
        self.assertIsNotNone(word.modified)