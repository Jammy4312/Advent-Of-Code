#!/usr/bin/env python3

#Advent of Code
#Day 1, Part 1
#Solution by James C. (https://github.com/JamesMCo)

import unittest

def solve(puzzle_input):
    total = 0

    for i, x in enumerate(puzzle_input):
        if puzzle_input[i] == puzzle_input[(i+1) % len(puzzle_input)]:
            total += int(x)

    return total

def main():
    f = open("puzzle_input.txt")
    puzzle_input = f.read()[:-1]
    f.close()

    total = solve(puzzle_input)

    print("The solution to the captcha is " + str(total) + ".")

class AOC_Tests(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(solve("1122"), 3)

    def test_ex2(self):
        self.assertEqual(solve("1111"), 4)

    def test_ex3(self):
        self.assertEqual(solve("1234"), 0)

    def test_ex4(self):
        self.assertEqual(solve("91212129"), 9)

if __name__ == "__main__":
    if unittest.main(verbosity=2, exit=False).result.wasSuccessful():
        main()
        exit(0)
    else:
        exit(1)
