import datetime

from django.utils import timezone
from django.test import TestCase
from .models import Question


class QuestionModelsTests(TestCase):
    def test_was_published_recently_with_future_pub_date(self):
        future_time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=future_time)
        actual = future_question.was_published_recently()
        expected = False
        self.assertIs(actual, expected)

    def test_was_published_recently_with_old_pub_date(self):
        old_time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=old_time)
        actual = old_question.was_published_recently()
        expected = False
        self.assertIs(actual, expected)

    def test_was_published_recently_with_recent_pub_date(self):
        recent_time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=recent_time)
        actual = recent_question.was_published_recently()
        expected = True
        self.assertIs(actual, expected)
