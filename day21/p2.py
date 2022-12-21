from sympy import symbols, solve_linear

l = open("input.txt").read().splitlines()
l = [x.split(": ") for x in l]
rawMonkeys={}
for x in l:
    if len(x[1])>5:
        x[1] = x[1].split(' ')
    rawMonkeys[x[0]] = x[1]

humn = symbols("humn")


def Find(name):
    if name == "humn":
        return humn
    if type(rawMonkeys[name]) == str: 
        return int(rawMonkeys[name])
    else:
        
        num1 = Find(rawMonkeys[name][0])
        operator = rawMonkeys[name][1]
        num2 = Find(rawMonkeys[name][2])
        return Calc(num1,num2,operator)

def Calc(n1,n2,op):
    return eval(f'({n1}) {op} ({n2})')


left = Find(rawMonkeys["root"][0])
right = Find(rawMonkeys["root"][2])
print(left,'=',right)

ans = round(solve_linear(left, right)[1])
print(f"part 2: {ans}")
#print(f"part 1: {round(monkeys['root'])}")




        
    

print(Calc(2,3,'=='))#3379022190351