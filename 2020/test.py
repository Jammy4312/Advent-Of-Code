#!/usr/bin/env python3

import colorama, os

colorama.init()

if os.name == "nt":
    s = ""
else:
    s = "python ./"

names = ["",
         "Report Repair", "Password Philosophy", "Toboggan Trajectory", "Passport Processing", "Binary Boarding",
         "Custom Customs", "Handy Haversacks", "Handheld Halting", "Encoding Error", "Adapter Array",
         "Seating System", "Rain Risk", "Shuttle Search", "Docking Data", "Rambunctious Recitation",
         "Ticket Translation", "Conway Cubes", "Operation Order", "Monster Messages", "Jurassic Jigsaw",
         "Allergen Assessment", "", "", "", ""]

printed = False
p_day   = False
for day in range(1, 26):
    if os.path.isdir(str(day).zfill(2)):
        os.chdir(str(day).zfill(2))
        if os.path.isfile("Part1.py"):
            if printed:
                print("\n")
            sep = "*" * len(f"**  Day {day}  - {names[day]}  **")
            print(f"{colorama.Fore.YELLOW}{sep}{colorama.Fore.RESET}\n{colorama.Fore.YELLOW}**  Day {day}  - {names[day]}  **{colorama.Fore.RESET}\n{colorama.Fore.YELLOW}{sep}{colorama.Fore.RESET}\n\n\n{colorama.Fore.GREEN}Testing Part 1{colorama.Fore.RESET}\n")
            p_day = True
            
            r = os.system(s + "Part1.py")
            if r:
                exit(r)

            printed = True
        if os.path.isfile("Part2.py"):
            if printed:
                print("\n")
            if not p_day:
                sep = "*" * len(f"**  Day {day}  - {names[day]}  **")
                print(f"{colorama.Fore.YELLOW}{sep}{colorama.Fore.RESET}\n{colorama.Fore.YELLOW}**  Day {day}  - {names[day]}  **{colorama.Fore.RESET}\n{colorama.Fore.YELLOW}{sep}{colorama.Fore.RESET}\n\n\n{colorama.Fore.GREEN}Testing Part 2{colorama.Fore.RESET}\n")
            else:
                print(f"{colorama.Fore.GREEN}Testing Part 2{colorama.Fore.RESET}\n")
            
            r = os.system(s + "Part2.py")
            if r:
                exit(r)

            printed = True
        os.chdir("..")
