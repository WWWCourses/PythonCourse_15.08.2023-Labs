from re import U
import unittest
from parameterized import parameterized
import os, sys

# # Navigate to the script's directory
script_dir = os.path.dirname(__file__)
# Add the project root to the system path
sys.path.append(os.path.join(script_dir, '..'))

from regex_exercises.main import is_valid_username, custom_capitalization, uppercase_I

class TestUsernameValidation(unittest.TestCase):
	@parameterized.expand([
		("User123", True),
		("Valid-User_123", True),
		("u1234567890123", True),
		("u____a", True),
		("us", False),
		("user_name_with_long_length", False),
		("1username", False),
		("_username", False),
		("username-", False),
		("username_", False),
		("User@name-", False)
	])
	def test_valid_usernames(self, username, result):
		self.assertEqual(is_valid_username(username), result)

class TestCustomCapitalization(unittest.TestCase):

    @parameterized.expand([
        ("an apple a day keeps the doctor away", "a", "An Apple a day keeps the doctor Away"),
        ("random words in a sentence", "r", "Random words in a sentence"),
        ("capitalize multiple As", "a", "capitalize multiple As"),
        ("no matching letters", "z", "no matching letters"),
        # Add more test cases as needed
    ])
    def test_custom_capitalization(self, input_str, letter, expected_output):
        self.assertEqual(custom_capitalization(input_str, letter), expected_output)

class TestUppercase_I(unittest.TestCase):
        @parameterized.expand([
            ('i\'m good tgennis player, my god', 'I\'m good tgennis player, my God'),
            ('george', 'George')
        ])
        def test_uppercase_I(self,input_str, expected_output):
            self.assertEqual(uppercase_I(input_str), expected_output)


if __name__=='__main__':
	unittest.main(verbosity=2)