from itertools import groupby, filterfalse, tee
import unittest


def flip_bit_to_win(x: int) -> int:
    if x == 0:
        return 1
    # Create groups [('0', c_0), ('1', c_1), ('0', c_2), ... , ('1', c_{b-1}), ('0', c_b)]
    groups = [(digit, len(list(group))) for digit, group in groupby('0' + bin(x)[2:] + '0')]
    # Filter out groups with ('0', 1)
    filtered = list(filterfalse(lambda x: x[0] == '0' and x[1] <= 1, groups))
    # Find max individual length
    max_len = max(x[1] for x in filtered if x[0] == '1') + 1
    # Find max pairwise sum
    for a, b in pairwise(filtered):
        if a[0] == b[0] == '1' and a[1] + b[1] + 1 > max_len:
            max_len = a[1] + b[1] + 1
    return max_len


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


class TestOneAway(unittest.TestCase):
    def test_equal1(self):
        N = 0b11011101111
        answer = 8
        self.assertEqual(flip_bit_to_win(N), answer)

    def test_equal2(self):
        # This number is 11 bits long, but it's preceded by zeros. We can flip a zero at the beginning to make the
        # sequence 12 bits long
        N = 0b11111111111
        answer = 12
        self.assertEqual(flip_bit_to_win(N), answer)

    def test_equal3(self):
        # This number is 11 bits long, but it's preceded by zeros. We can flip a zero at the beginning to make the
        # sequence 12 bits long
        N = 0b0
        answer = 1
        self.assertEqual(flip_bit_to_win(N), answer)

    def test_equal4(self):
        # This number is 11 bits long, but it's preceded by zeros. We can flip a zero at the beginning to make the
        # sequence 12 bits long
        N = 0b1001
        answer = 2
        self.assertEqual(flip_bit_to_win(N), answer)

    def test_equal5(self):
        # This number is 11 bits long, but it's preceded by zeros. We can flip a zero at the beginning to make the
        # sequence 12 bits long
        N = 0b100111011
        answer = 6
        self.assertEqual(flip_bit_to_win(N), answer)


if __name__ == '__main__':
    unittest.main()
