import unittest
from src.y_2019.day_1 import parse, solve


class DayOneTestCase(unittest.TestCase):
    def test_parse(self):
        data = parse('''+1
        +2
        +3'''.split())
        self.assertEqual([1, 2, 3], data)

    def test_solve(self):
        data = [5, 20, 345]
        self.assertEqual(116, solve(data))

    def test_pass(self):
        input_f = open("input.txt", "r")
        data = parse(input_f.readlines())
        input_f.close()
        answer = solve(data)
        self.assertEqual(3161483, answer)


if __name__ == '__main__':
    unittest.main()
