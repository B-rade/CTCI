import unittest
from typing import Dict


def is_permutation(_input_1: str, _input_2: str) -> bool:
    if len(_input_1) != len(_input_2):
        return False
    count_1 = get_letter_count(_input_1)
    count_2 = get_letter_count(_input_2)
    return count_1 == count_2


def alternate_is_permutation(_input_1: str, _input_2: str) -> bool:
    if len(_input_1) != len(_input_2):
        return False
    return sorted(_input_1) == sorted(_input_2)


def get_letter_count(_input: str) -> Dict[str, int]:
    counter = dict()
    for letter in _input:
        if counter.get(letter):
            counter[letter] += 1
        else:
            counter[letter] = 1
    return counter


class TestIsPermutation(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_permutation('test', 'estt'))

    def test_false_not_same_length(self):
        self.assertFalse(is_permutation('test', 'te'))

    def test_false_not_permutation(self):
        self.assertFalse(is_permutation('test1', 'test2'))


class TestAlternateIsPermutation(unittest.TestCase):
    def test_true(self):
        self.assertTrue(alternate_is_permutation('test', 'estt'))

    def test_false_not_same_length(self):
        self.assertFalse(alternate_is_permutation('test', 'te'))

    def test_false_not_permutation(self):
        self.assertFalse(alternate_is_permutation('test1', 'test2'))


if __name__ == '__main__':
    unittest.main()
