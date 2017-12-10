#!/usr/bin/env python3

#Advent of Code
#Day 10, Part 1
#Solution by James C. (https://github.com/JamesMCo)

import unittest

def rotate(l, n):
    t = [x for x in l]
    if len(t) <= 1:
        return t
    if len(t) == 2:
        return t[1] + t[0]
    for i in range(n):
        t = t[1:] + [t[0]]
    return t

def solve(puzzle_input, size=256):
    l = [x for x in range(size)]
    skip_size = 0

    for i in puzzle_input:
        if i <= size:
            l = l[i-1::-1] + l[i:]
        else:
            l = l[::-1]
        l = rotate(l, i + skip_size)
        skip_size += 1

    for i in puzzle_input:
        l = rotate(l, size - i + 1)
    return l[0] * l[1]

def main():
    f = open("puzzle_input.txt")
    puzzle_input = [int(x) for x in f.read()[:-1].split(",")]
    f.close()

    product = solve(puzzle_input)

    print("The result of multiplying the first two numbers in the list is " + str(product) + ".")

class AOC_Tests(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(solve([3, 4, 1, 5], 5), 12)

if __name__ == "__main__":
    if unittest.main(verbosity=2, exit=False).result.wasSuccessful():
        main()
        exit(0)
    else:
        exit(1)