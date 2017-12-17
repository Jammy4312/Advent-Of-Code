#!/usr/bin/env python3

#Advent of Code
#Day 16, Part 2
#Solution by James C. (https://github.com/JamesMCo)

import unittest

def solve(puzzle_input, size=16, iters=1000000000):
    programs = [chr(x + 97) for x in range(size)]
    initial = programs[:]
    remaining = iters
    
    while remaining != 0:
        for move in puzzle_input:
            if move[0] == "s":
                for i in range(int(move[1:])):
                    programs.insert(0, programs.pop())
            elif move[0] == "x":
                programs[int(move.split("/")[0][1:])], programs[int(move.split("/")[1])] = programs[int(move.split("/")[1])], programs[int(move.split("/")[0][1:])]
            elif move[0] == "p":
                programs = "".join(programs)
                programs = programs.replace(move[1], "!").replace(move[3], move[1]).replace("!", move[3])
                programs = list(programs)
        remaining -= 1
        if programs == initial:
            remaining = iters % (iters-remaining)
        

    return "".join(programs)

def main():
    f = open("puzzle_input.txt")
    puzzle_input = f.read()[:-1].split(",")
    f.close()

    order = solve(puzzle_input)

    print("The order of the programs after the dance is " + str(order) + ".")

class AOC_Tests(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(solve(["s1", "x3/4", "pe/b"], 5, 2), "ceadb")

    def test_ex2(self):
        self.assertEqual(solve(["s1"], 5, 12), "deabc")

    def test_ex3(self):
        self.assertEqual(solve(["s1"], 5, 5), "abcde")

if __name__ == "__main__":
    if unittest.main(verbosity=2, exit=False).result.wasSuccessful():
        main()
        exit(0)
    else:
        exit(1)