# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

import unittest

class TestBasic(unittest.TestCase):
    "Basic tests"

    def test_basic(self):
        a = 1
        self.assertEqual(1, a)

    def test_basic_2(self):
        a = 1
        assert a == 1


from django.test import TestCase
from review.models import Review

class ReviewTestCase(TestCase):

    def setUp(self):
        Review.objects.create(old_id="12",date="lion", salary="roar",type="",employee="position")
        Review.objects.create(old_id="13",date="hack", salary="tomuch",type="lost",employee="lost")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        review1 = Review.objects.get(date="lion")
        review2 = Review.objects.get(date="hack")
        self.assertEqual(review1, 'The lion says "roar"')
        self.assertEqual(review2, 'The cat says "meow"')
