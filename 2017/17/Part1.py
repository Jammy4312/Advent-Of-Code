#!/usr/bin/env python3

#Advent of Code
#Day 17, Part 1
#Solution by James C. (https://github.com/JamesMCo)

import unittest

def solve(puzzle_input):        
    buffer = [0]
    current = 0

    for i in range(1, 2018):
        current = (current + puzzle_input) % len(buffer) + 1
        buffer.insert(current, i)

    return buffer[(buffer.index(2017) + 1) % len(buffer)]

def main():
    f = open("puzzle_input.txt")
    puzzle_input = int(f.read()[:-1])
    f.close()

    value = solve(puzzle_input)

    print("The value after the last value written is " + str(value) + ".")

class AOC_Tests(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(solve(3), 638)

if __name__ == "__main__":
    if unittest.main(verbosity=2, exit=False).result.wasSuccessful():
        main()
        exit(0)
    else:
        exit(1)