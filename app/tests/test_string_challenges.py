import unittest

from app.code.string_challenges import remove_vowels, remove_numbers, \
        remove_punctuation, is_palindrome


class StringChallengeTest(unittest.TestCase):

    def test_remove_vowels(self):
        self.assertEqual(remove_vowels("Hello"), "Hll")
        self.assertEqual(remove_vowels("Take me home"), "Tk m hm")

    def test_remove_numbers(self):
        self.assertEqual(remove_numbers("ABC123"), "ABC")
        self.assertEqual(remove_numbers("You got 1 shot"), "You got  shot")

    def test_remove_punctuation(self):
        self.assertEqual(remove_punctuation("Yikes!!!"), "Yikes")
        self.assertEqual(remove_punctuation("Well, here it is: right?"),
                "Well here it is right")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("RaCecar"))
        self.assertFalse(is_palindrome("Hello"))
