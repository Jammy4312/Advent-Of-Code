#!/usr/bin/env python3

#Advent of Code
#Day 12, Part 1
#Solution by Jammy4312 (https://jammy4312.me)

f = open("puzzle_input.txt")
puzzle_input = f.read()[0:-1]
f.close()

total = 0

puzzle_input = puzzle_input.replace("[", ",").replace("]", ",")
puzzle_input = puzzle_input.replace("{", ",").replace("}", ",")
puzzle_input = puzzle_input.replace(":", ",").replace(";", ",")

for i in puzzle_input.split(","):
    try:
        total += int(i)
    except ValueError:
        pass

print("The final total is: " + str(total))
