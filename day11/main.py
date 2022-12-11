import math

with open("input.txt") as f:
    lines = f.read().splitlines()
lines.append('Monkey') # to ssave last monkey inside the  loop

def Beolvas():
    monkeys = [] #[ [ items(int), operation, test(int), [if1, if2](int), ins_times ] ]
    #---------------------0-----------1----------2----------3----------------4--------
    if_true_false = []
    sv=[]
    for x in lines:
        if 'Monkey' in x and len(sv)>0:
            sv.append(if_true_false)
            sv.append(0)
            monkeys.append(sv)
            if_true_false,sv=[],[]
        elif 'Starting' in x:
            sv.append(list(map(int,x.split(':')[1].split(', '))))
        elif 'Operation' in x:
            sv.append(x.split('= old ')[1].split(' '))
        elif 'Test' in x:
            sv.append(int(x.split('by ')[1]))
        elif 'If' in x:
            if_true_false.append(int(x.split('monkey ')[1]))
    return monkeys

def Solve(monkeys,n,p1):
    mod = 1
    for m in monkeys:
        mod *= m[2]
    for _ in range(n):
        i = 0
        for items,op,test,ifs,freq in monkeys:
            for item in items:
                monkeys[i][4]+=1
                monkeys[i][0] = monkeys[i][0][1:]
                new_worry_lvl = -1
                if op[0] == '*' and op[1]=='old':
                    new_worry_lvl = item*item
                elif op[0] == '*':
                    new_worry_lvl = item*int(op[1])
                elif op[0] == '+':
                    new_worry_lvl = item+int(op[1])
                if p1:
                    bored_lvl = math.floor(new_worry_lvl/3)
                else:
                    bored_lvl = new_worry_lvl %mod
                
                if bored_lvl % test == 0:
                    monkeys[ifs[0]][0].append(bored_lvl)
                else:
                    monkeys[ifs[1]][0].append(bored_lvl)
            i+=1
    p1 = list(reversed(sorted([m[4] for m in monkeys])))
    return p1[0]*p1[1]

print(f"part 1: {Solve(Beolvas(),20,True)}")
print(f"part 2: {Solve(Beolvas(),10000,False)}")

        

    