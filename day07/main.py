with open("input.txt") as f:
    lines = f.read().splitlines()

def SolveFolders(lines):
    sizes={'/':0}
    current_location = ["/"]
    for line in lines:
        cmd = line.split()
        if line[0] == '$' and cmd[1] == 'cd': #ha change directory
            if cmd[2]== '..' and len(current_location) > 1:#ha jump back
                current_location.pop(-1)
            else:
                if cmd[2] != '/':
                    current_location.append(current_location[-1]+cmd[2])
                if current_location[-1] not in sizes.keys():
                    sizes[current_location[-1]]=0
        elif cmd[0] != 'dir' and cmd[1]!='ls': #starts with number
            for x in current_location:
                sizes[x] += int(cmd[0])
    return sizes

sizes = SolveFolders(lines)
high_to_low_folders = sorted(list(sizes.values()))
high_to_low_folders.reverse()

def Part1(htl_folders):
    return sum(x for x in htl_folders if x <= 100000)

def Part2(htl_folders,sizes):
    return min(x for x in htl_folders if x >= sizes['/']-40000000)

print(f"part 1: {Part1(high_to_low_folders)}")     
print(f"part 2: {Part2(high_to_low_folders,sizes)}")