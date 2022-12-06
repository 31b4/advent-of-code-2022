with open("input.txt") as f:
    raw_lines = f.read()

def PartN(n):
    for i in range(n,len(raw_lines)):
        if len(set(raw_lines[i-n:i])) == n:
            return i
print(f"Part 1: {PartN(4)}")
print(f"Part 2: {PartN(14)}")