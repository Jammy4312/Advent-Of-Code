#!/usr/bin/env python3

#Advent of Code
#Day 2, Part 2
#Solution by James C. (https://github.com/JamesMCo)

import os, sys, colorama, time
sys.path.append(os.path.abspath("../.."))
import unittest, util.tests

from itertools import combinations

def solve(puzzle_input):
    for pair in combinations(puzzle_input, 2):
        diff = 0
        last_index = None

        for i, c in enumerate(pair[0]):
            if c != pair[1][i]:
                diff += 1
                last_index = i

        if diff == 1:
            return pair[0][:last_index] + pair[0][last_index+1:]

def main():
    f = open("puzzle_input.txt")
    puzzle_input = f.read()[:-1].split("\n")
    f.close()

    letters = solve(puzzle_input)

    print("The letters in common are " + str(letters) + ".")

class AOC_Tests(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(solve(["abcde",
                                "fghij",
                                "klmno",
                                "pqrst",
                                "fguij",
                                "axcye",
                                "wvxyz"]), "fgij")

if __name__ == "__main__":
    if unittest.main(verbosity=2, exit=False, testRunner=util.tests.Runner).result.wasSuccessful():
        start = time.time()
        main()
        end = time.time()
        print(f"{colorama.Fore.CYAN}Solution found in {colorama.Fore.GREEN}{round(end - start, 3)}s{colorama.Fore.CYAN}.{colorama.Fore.RESET}")
        exit(0)
    else:
        exit(1)