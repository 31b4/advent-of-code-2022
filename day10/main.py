with open("input.txt") as f:
    l = f.read().splitlines()

values=[1]
sm = 0
sv=1
crt = [[" " for x in range(40)] for y in range(6)]
def check():
    global values, sm, sv
    cnt = len(values)
    if cnt == 20 or cnt == 60 or cnt == 100 or cnt == 140 or cnt == 180 or cnt == 220:
        sm += cnt * sv
    if abs((cnt-1)%40-sv) < 2:
        crt[(cnt-1)//40][(cnt-1)%40] = "#"
for i in range(len(l)):
    x= l[i].split(' ')
    check()
    values.append(values[-1])
    if x[0]!='noop':
        add = int(x[1])
        check()
        values.append(values[-1] + add)
        sv+=int(x[1])

print(f"part 1: {sm}")
print("part 2: ")
for line in crt:
	print("".join(line))
