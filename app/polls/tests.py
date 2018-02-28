import datetime

from django.utils import timezone
from django.test import TestCase
from .models import Question
from django.urls import reverse


def create_question(question_text, days):
    """
    returns `Question` object with specified `question_text` and `pub_date`
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available.')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question(self):
        create_question(question_text='future question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available.')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        question_text = 'past question'
        create_question(question_text=question_text, days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, question_text)
        self.assertQuerysetEqual(response.context['latest_question_list'], [
                                 '<Question: past question>'])

    def test_future_question_and_past_question(self):
        future_question_text = 'future question'
        create_question(question_text=future_question_text, days=30)
        past_question_text = 'past question'
        create_question(question_text=past_question_text, days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, future_question_text)
        self.assertContains(response, past_question_text)
        self.assertQuerysetEqual(response.context['latest_question_list'], [
                                 '<Question: past question>'])

    def test_two_past_questions(self):
        question_text_1 = 'past question 1'
        create_question(question_text=question_text_1, days=-30)
        question_text_2 = 'past question 2'
        create_question(question_text=question_text_2, days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, question_text_1)
        self.assertContains(response, question_text_2)
        self.assertQuerysetEqual(response.context['latest_question_list'], [
                                 '<Question: past question 2>', '<Question: past question 1>'])


class QuestionModelsTests(TestCase):
    def test_was_published_recently_with_future_pub_date(self):
        future_time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=future_time)
        actual = future_question.was_published_recently()
        expected = False
        self.assertIs(actual, expected)

    def test_was_published_recently_with_past_pub_date(self):
        past_time = timezone.now() - datetime.timedelta(days=30)
        past_question = Question(pub_date=past_time)
        actual = past_question.was_published_recently()
        expected = False
        self.assertIs(actual, expected)

    def test_was_published_recently_with_recent_pub_date(self):
        recent_time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=recent_time)
        actual = recent_question.was_published_recently()
        expected = True
        self.assertIs(actual, expected)
