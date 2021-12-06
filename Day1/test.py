import unittest
from AdventOfCode.Day1.SonarSweeper import sonar_sweeper, sonar_sweeper_advanced


class MyTestCase(unittest.TestCase):
    def test_sonar_sweeper(self):
        input = [199,200,208,210,200,207,240,269,260,263]
        output = 7
        pred = sonar_sweeper(input)
        self.assertEqual(pred, output, f"Prediction is {pred} output is {output}. This is not correct.")

    def test_day1(self):
        input = []
        with open('input_day1.txt') as f:
            for line in f:
                input.append(int(line))
        output = sonar_sweeper(input)
        print(output)

    def test_day1_advanced(self):
        input = []
        with open('input_day1.txt') as f:
            for line in f:
                input.append(int(line))
        output = sonar_sweeper_advanced(input)
        print(output)


if __name__ == '__main__':
    unittest.main()
