import unittest


def insert_binary_integers(N: int, M: int, i: int, j: int) -> int:
    mask = (~0 << (j+1)) | ((1 << i) - 1)
    result = N & mask
    result |= M << i
    return result

    # another way
    mask = ~(((1 << (j-i+1)) -1) << i)
    result = N & mask
    result |= M << i
    return result


class TestOneAway(unittest.TestCase):
    def test_true1(self):
        N = 0b1000000000
        M = 0b10011
        i = 2
        j = 6
        answer = 0b1001001100
        self.assertEqual(insert_binary_integers(N, M, i, j), answer)


if __name__ == '__main__':
    unittest.main()