import unittest


def one_away(string1: str, string2: str) -> bool:
    if string1 == string2:
        return True
    if abs(len(string1) - len(string2)) > 1:
        return False
    if len(string1) >= len(string2):
        longer_string = string1
        shorter_string = string2
    else:
        longer_string = string2
        shorter_string = string1
    mismatch_index = find_mismatch(longer_string, shorter_string)
    return longer_string[mismatch_index+1:] == shorter_string[mismatch_index:] or longer_string[mismatch_index+1:] == shorter_string[mismatch_index+1:]


def find_mismatch(string1: str, string2: str) -> int:
    for i in range(len(string1)):
        if i >= len(string2):
            return i
        elif string1[i] != string2[i]:
            return i


class TestOneAway(unittest.TestCase):
    def test_true1(self):
        self.assertTrue(one_away('pole', 'pale'))

    def test_true2(self):
        self.assertTrue(one_away('ple', 'pale'))

    def test_true3(self):
        self.assertTrue(one_away('pole', 'ple'))

    def test_true4(self):
        self.assertTrue(one_away('pole', 'paole'))

    def test_true5(self):
        self.assertTrue(one_away('poles', 'pole'))

    def test_false1(self):
        self.assertFalse(one_away('bole', 'bake'))


if __name__ == '__main__':
    unittest.main()