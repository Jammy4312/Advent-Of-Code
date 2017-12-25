#!/usr/bin/env python3

import colorama, os

if os.name == "nt":
    s = ""
else:
    s = "python ./"

sep = "*" * 28

printed = False
for day in range(1, 25):
    if day == 10:
        sep += "*"
    if os.path.isdir(str(day).zfill(2)):
        os.chdir(str(day).zfill(2))
        if os.path.isfile("Part1.py"):
            if printed:
                print("\n")
            print(f"{colorama.Fore.YELLOW}{sep}\n**  Testing Day {day} Part 1  **\n{sep}{colorama.Fore.RESET}\n")
            
            r = os.system(s + "Part1.py")
            if r:
                exit(r)

            printed = True
        if os.path.isfile("Part2.py"):
            if printed:
                print("\n")
            print(f"{colorama.Fore.YELLOW}{sep}\n**  Testing Day {day} Part 2  **\n{sep}{colorama.Fore.RESET}\n")
            
            r = os.system(s + "Part2.py")
            if r:
                exit(r)

            printed = True
        os.chdir("..")
