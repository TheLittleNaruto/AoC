import unittest
from src.y_2019.day_2 import parse, solve


class DayOneTestCase(unittest.TestCase):
    def test_parse(self):
        data = parse('1,2,3')
        self.assertEqual([1, 2, 3], data)

    def test_solve(self):
        data = [2, 3, 0, 3, 99]
        self.assertEqual(2, solve(data))

    def test_pass(self):
        input_f = open("input_2.txt", "r")
        data = parse(input_f.readline())
        input_f.close()
        answer = solve(data)
        self.assertEqual(250702, answer)


if __name__ == '__main__':
    unittest.main()
