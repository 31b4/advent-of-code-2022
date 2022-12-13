import json
inp = open('input.txt').read().split("\n\n")

def compare(first, second):
    if type(first) == int:
        if type(second) == int:
            if first < second:
                return -1
            elif first > second:
                return 1
            return 0
        else:
            first = [first]
    if type(second) == int:
        if type(first) == int:
            if first < second:
                return -1
            elif first > second:
                return 1
            return 0
        else:
            second = [second]
    for i in range(min(len(first), len(second))):
        res = compare(first[i], second[i])
        if res != 0:
            return res
    if len(first) < len(second):
        return -1
    if len(first) > len(second):
        return 1
    return 0

def Part1():
    ans = 0
    for i, l in enumerate(inp):
        ws = l.split("\n")
        if len(ws) == 2:
            first = json.loads(ws[0])
            second = json.loads(ws[1])
            if compare(first, second) == -1:
                ans += i+1
    return ans

def Part2():
    vs = []
    for l in inp:
        ws = l.split("\n")
        if len(ws) >= 2:
            first = json.loads(ws[0])
            second = json.loads(ws[1])
            vs.append(first)
            vs.append(second)
    vs.append([[2]])
    vs.append([[6]])
    sorted_vs = {}
    for x in vs:
        numberOfCorrect = 0
        for e in vs:
            if compare(e, x) == -1:
                numberOfCorrect +=1
        sorted_vs[numberOfCorrect] = x

    sorted_vs = dict(sorted(sorted_vs.items()))
    #dict_key of elements
    i_2 = list(sorted_vs.keys())[list(sorted_vs.values()).index([[2]])]+1 
    i_6 = list(sorted_vs.keys())[list(sorted_vs.values()).index([[6]])]+1
    return i_2*i_6

print(f"part 1 : {Part1()}")
print(f"part 2: {Part2()}")