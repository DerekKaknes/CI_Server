import string


def remove_vowels(s):
    """This function should remove all vowels (a,e,i,o,u) from the input
    string and return the result"""
    # Add your code
    string_without_vowels = ''.join([l for l in s if l.lower() not in 'aeiou'])
    return string_without_vowels


def remove_numbers(s):
    """This function should remove all numbers from the input string
    and return the result"""
    # Add your code
    string_without_numbers = ''.join([l for l in s if l not in string.digits])
    return string_without_numbers


def remove_punctuation(s):
    """This function should remove all punctuation marks from the input
    string and return the result.  HINT: see `string.punctuation` from the
    imported string module for characters that should be removed."""
    # Add your code
    string_without_punctuation = ''.join([l for l in s if l not \
            in string.punctuation])
    return string_without_punctuation


def is_palindrome(s):
    """A palindrome is a word that is spelled the same forwards and
    backwards.  This function should return either True or Fasle indicating
    whether the input string is a palindrome.  Note that capitalizations and
    punctuations can be ignored"""
    # Add your code
    forward = remove_punctuation(s.lower()).replace(' ', '')
    backward = forward[::-1]
    return forward == backward
