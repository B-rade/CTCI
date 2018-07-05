import unittest


def is_unique(_input: str) -> bool:
    if len(_input) > 128:
        return False
    visited = set()
    for letter in _input:
        if letter in visited:
            return False
        else:
            visited.add(letter)
    return True


def is_unique_no_data_structures(_input: str) -> bool:
    if len(_input) > 128:
        return False
    visited = 0
    for letter in _input:
        val = ord(letter) - ord('a')
        if visited & (1 << val):
            return False
        else:
            visited |= (1 << val)
    return True


class TestIsUnique(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_unique('abcdefghijklmnopqrstuvwxyz'))

    def test_false(self):
        self.assertFalse(is_unique('abcda'))


class TestIsUniqueNoDataStructure(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_unique_no_data_structures('abcdefghijklmnopqrstuvwxyz'))

    def test_false(self):
        self.assertFalse(is_unique_no_data_structures('abcda'))


if __name__ == '__main__':
    unittest.main()
