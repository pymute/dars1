def palindrome(n, m):
    for i in range(n, m+1):
        num_str = str(i)
        if num_str == num_str[::-1]:
            print(num_str, end=' ')

import unittest


class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertEqual(palindrome(10, 100), '11 22 33 44 55 66 77 88 99 ')
        self.assertEqual(palindrome(200, 300), '202 212 222 232 242 252 262 272 282 292 ')
        self.assertEqual(palindrome(500, 600), '505 515 525 535 545 555 565 575 585 595 ')
        self.assertEqual(palindrome(1, 9), '1 2 3 4 5 6 7 8 9 ')

unittest.main(argv=[''], exit=False)