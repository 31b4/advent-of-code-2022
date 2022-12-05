
with open("input.txt") as f:
    raw_stacks, raw_lines = f.read().split("\n\n")
    lines = raw_lines.splitlines()

def StacksConverter(stacksCount): #[[A,B],[C,D]] by stack bottom to top
    stacks = [[] for _ in range(stacksCount)]  # stacksCount * []
    stacks2 = [[] for _ in range(stacksCount)]  
    for row in raw_stacks.splitlines()[-2::-1]:
        for i,c in enumerate(row[1::4]):
            if c!=" ": 
                stacks[i].append(c)
                stacks2[i].append(c)
    return stacks,stacks2

def LinesConverter(): #[[2,1,3],[1,2,1]] steps
    steps = []
    for line in lines:
        _,m,_,f,_,t = line.split()#move,n,from,s,to,d
        steps.append(list(map(int,(m,f,t))))
    return steps

def Part1_2(stacksCount):
    stacks,stacks2 = StacksConverter(stacksCount)
    steps = LinesConverter()
    for m,f,t in steps:
        for i in range(m):
            stacks[t-1].append(stacks[f-1].pop())#t-1,f-1 : index from 0
        stacks2[t-1].extend(stacks2[f-1][-m:])
        del stacks2[f-1][-m:]
    return "".join(s[-1] for s in stacks),"".join(f[-1] for f in stacks2)

#test = Part1_2(3)
#print(f"part 1: {test[0]}")
#print(f"part 2: {test[1]}")

ans = Part1_2((len(raw_stacks.splitlines()[-1])+1)//4)#9 stocks
print(f"part 1: {ans[0]}")
print(f"part 2: {ans[1]}")