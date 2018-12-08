def as_string():
    with open("puzzle_input.txt") as f:
        return f.read().strip()

def as_lines():
    with open("puzzle_input.txt") as f:
        return f.read().strip().split("\n")

def as_int():
    with open("puzzle_input.txt") as f:
        return int(f.read().strip())

def as_int_list(delim):
    with open("puzzle_input.txt") as f:
        return [int(x) for x in f.read().strip().split(delim)]