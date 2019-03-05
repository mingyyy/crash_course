import text
import unittest


class TestText(unittest.TestCase):

    def setUp(self): # will be created before each test
        self.my_list = [1,2,3,4]

    def tearDown(self): # after every test runs
        pass


    # is_palindrome returns False if ""
    def test_if_input_to_is_palindrome_is_empty(self):
        self.assertFalse(text.is_palindrome(""))

    # is_palindrome returns False if ""
    def test_if_input_to_is_palindrome_is_space(self):
        self.assertIs(text.is_palindrome("         "), False)
        self.assertIs(text.is_palindrome(" "), False)

    # is_palindrome returns True single char
    def test_if_input_to_is_palindrome_is_one_char(self):
        self.assertTrue(text.is_palindrome("a"))
    # is_palindrome returns True if word that's longer than one char is the same forward and backward
    # return False if  string contains a number

    def test_if_input_to_is_palindrome_is_working(self):
        self.assertTrue(text.is_palindrome("ana"))
        self.assertTrue(text.is_palindrome("1234321"))
        self.assertFalse(text.is_palindrome("martin"))


if __name__ == '__main__':
    unittest.main()
