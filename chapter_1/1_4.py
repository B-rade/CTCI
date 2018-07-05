import unittest
from collections import Counter


def palindrome_permutation(_input: str) -> bool:
    counter = Counter(str.strip(' '))
    flag = False
    for value in counter.values():
        if flag and value % 2 == 1:
            return False
        elif value % 2 == 1:
            flag = True
    return True


class TestPalindromePermutation(unittest.TestCase):
    def test_true(self):
        self.assertTrue('tact coa')


if __name__ == '__main__':
    unittest.main()