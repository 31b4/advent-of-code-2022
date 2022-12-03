
with open("input.txt") as f:
    data = f.read().splitlines()

def convertToNum(x):
    if x >= 'a' and x <= 'z':
        return ord(x)-ord('a') +1
    else:
        return ord(x)-ord('A') + 27

def part1(data):
    sum = 0
    for x in data:
        a = set(x[:len(x)//2]).intersection(set(x[len(x)//2:]))
        a = a.pop()#set to char
        sum += convertToNum(a)
    return sum

def part2(data):
    sum = 0
    for x in data:
        a =set(x[0]).intersection(set(x[1])).intersection(set(x[2]))
        a = a.pop()
        sum += convertToNum(a)
    return(sum)


print(f"part 1: {part1(data)}")
print(f"part 2: {part2(zip(*[iter(data)]*3))}")