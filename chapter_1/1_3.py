import unittest


def urlify(_input: str, _len_of_string: int) -> str:
    return _input.strip().replace(' ', '%20')


class TestUrlify(unittest.TestCase):
    def test_true(self):
        self.assertTrue(urlify('Mr John Smith   ', 13), 'Mr%20John%20Smith')


if __name__ == '__main__':
    unittest.main()