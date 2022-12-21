l = open("input.txt").read().splitlines()
l = [x.split(": ") for x in l]
rawMonkeys={}
for x in l:
    if len(x[1])>5:
        x[1] = x[1].split(' ')
    rawMonkeys[x[0]] = x[1]

def Find(name):

    if type(rawMonkeys[name]) == str: 
        return int(rawMonkeys[name])
    else:
        
        num1 = Find(rawMonkeys[name][0])
        operator = rawMonkeys[name][1]
        num2 = Find(rawMonkeys[name][2])
        return Calc(num1,num2,operator)

def Calc(n1,n2,op):
    return eval(f'{n1} {op} {n2}')

#solve all-------------
monkeys = {}
for x in l:
    if type(x[1])==str:
        monkeys[x[0]]=int(x[1])
    else:
        num1 = Find(x[1][0])
        operator = x[1][1]
        num2 = Find(x[1][2])
        monkeys[x[0]]=Calc(num1,num2,operator)

#solve just root-----------
print(f"part 1: {round(Find('root'))}")


#part2------------would work if answer would be lower (part 2 in p2.py)
rawMonkeys["root"][1] = "=="
for i in range(3379022190351,3379022190353):
    rawMonkeys["humn"] = str(i)
    if Find("root") is True:
        print(f"part 2: {i}")
