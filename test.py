#!/usr/bin/env python
# -*- coding: utf-8 -*-u

"""
Purpose : Some tests for the HaveiBeenPwnedApi class

To run the tests : $ python -m unittest -v test
"""

import unittest
from pwnedapi import HaveIBeenPwnedApi
from exception import NotValidEmail, BreachNotFound, UnvalidParameters

class TestHaveIBeenPwnedApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ creating test data set for the test module """
        cls.api = HaveIBeenPwnedApi()

    def test_get_all_dataclasses(self):
        dataclasses = self.api.get_all_dataclasses()
        self.assertIn("Email addresses", dataclasses)
        self.assertIn("Passwords", dataclasses)
        self.assertIn("Usernames", dataclasses)
        self.assertNotIn("Adobe", dataclasses)

    def test_get_all_breaches_name(self):
        breaches = self.api.get_all_breaches_name()
        self.assertIn("AshleyMadison", breaches)
        self.assertIn("Adobe", breaches)
        self.assertNotIn("Google", breaches)

    def test_get_breach(self):
        self.assertEqual("AshleyMadison", self.api.get_breach("AshleyMadison")['Name'])
        self.assertIsInstance(self.api.get_breach("AshleyMadison"), dict)
        self.assertRaises(BreachNotFound, self.api.get_breach, "Google")

    def test_regex_email(self):
        self.assertTrue(self.api.regex_email.match("ericfourrier0@gmail.com"))
        self.assertIsNone(self.api.regex_email.match("tvhmxoleoubgmail.com"))

    def test_check_email(self):
        self.assertEqual(self.api.check_email("ericfourrier0@gmail.com"), [])
        self.assertEqual(self.api.check_email("ericfourrier1@hotmail.com"), [])
        self.assertRaises(NotValidEmail, self.api.check_email, "tvhmxoleoubgmail.com")

    def test_check_pastebin(self):
        self.assertEqual(self.api.check_pastebin("ericfourrier0@gmail.com"), [])
        self.assertEqual(self.api.check_pastebin("ericfourrier1@hotmail.com"), [])
        self.assertNotEqual(self.api.check_pastebin("tvhmxoleoub@gmail.com"), [])
        self.assertRaises(NotValidEmail, self.api.check_pastebin, "tvhmxoleoubgmail.com")
