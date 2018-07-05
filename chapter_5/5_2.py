import unittest


def binary_to_string(x: float) -> str:
    if not (0 < x < 1):
        return 'ERROR'

    result = []
    while x > 0:
        if len(result) >= 32:
            return 'ERROR'
        x *= 2
        if x >= 1:
            result.append('1')
            x -= 1
        else:
            result.append('0')
    return ''.join(result)



class TestOneAway(unittest.TestCase):
    def test_equal1(self):
        N = 0.75
        answer = '11'
        self.assertEqual(binary_to_string(N), answer)

    def test_equal2(self):
        N = 0.5
        answer = '1'
        self.assertEqual(binary_to_string(N), answer)

    def test_equal3(self):
        N = 0.6875
        answer = '1011'
        self.assertEqual(binary_to_string(N), answer)

    def test_equal4(self):
        N = 0.123456789
        answer = 'ERROR'
        self.assertEqual(binary_to_string(N), answer)


if __name__ == '__main__':
    unittest.main()
