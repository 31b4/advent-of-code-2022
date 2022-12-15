import re
# PLEASE dont use my code, its fast as the fastest code in Ohio

l  = open('input.txt').readlines()
l[len(l)-1]+="\n"
def ReadSave():
    sensors = []
    beacons= []
    grid={}
    for line in l:
        sx, sy, bx, by = list(map(int, re.findall(r'(?<=\=)(.*?)(?=,|\:|\n)', line)))
        sensors.append((sx,sy))
        beacons.append((bx,by))
        grid[(sx,sy)]= 'S'
        grid[(bx,by)]= 'B'
    return sensors,beacons,grid

def DrawGrid(grid):
    for y in range(-3,23):
    #for y in range(0,21):
        print(y,"\t", end='')
        for x in range(min(grid)[0],max(grid)[0]):
        #for x in range(0,21):
            if grid.get((x,y)) == 'S':
                print("S",end="")
            elif grid.get((x,y)) == '#':
                print("#",end="")
            else:
                print("B" if (x, y) in grid else ".", end="")
        print()
    print()

def Manhattan(x1,y1,x2,y2):
    return int(abs(x2-x1)+abs(y2-y1))

def ClosestBeacon(x,y,beacons):
    min = 9999999999999999
    beacon = (None,None)
    for b in beacons:
        m = Manhattan(x,y,b[0],b[1])
        if m < min:
            min = m
            beacon = b
    return beacon,min

def Part1(grid,sensors,n):
    sensorsRange = []
    for s in sensors:
        sensorsRange.append(ClosestBeacon(s[0],s[1],beacons)[1])
    p1 = 0
    for x in range((min(grid)[0]-1000000),(max(grid)[0])+1000000):
        if grid.get((x,n)) != 'B' and grid.get((x,n)) != 'S':
            for i,sr in enumerate(sensorsRange):
                if Manhattan(x,n,sensors[i][0],sensors[i][1]) <= sr:
                    p1+=1
                    break
    return p1

# ------------------visualization------------------
def SlowBejaras(sensors,beacons,grid): #another solve for part1, only works for example
    for s in sensors:
        edges = [s]
        found = False
        sv = []
        while not found:
            if len(sv)!=0:
                edges = sv
            sv = []  
            for x,y in edges:
                for d in [[-1,0],[1,0],[0,-1],[0,1]]:
                    sv.append((x+d[0],y+d[1]))
                    if grid.get((x+d[0],y+d[1])) == '#':
                        continue
                    elif grid.get((x+d[0],y+d[1])) != 'B':
                        if grid.get((x+d[0],y+d[1])) != 'S':
                            grid[(x+d[0],y+d[1])] = '#'
                    else:
                        found = True
    p1 =0
    for x in range(min(grid)[0],max(grid)[0]):
        if grid.get((x,2000000)) == '#':
            p1+=1
  
sensors,beacons,grid = ReadSave()
#SlowBejaras(sensors,beacons,grid)
#DrawGrid(grid)

print(f"part 1: {Part1(grid,sensors,2000000)}")
#print(f"part 1: {Part1(grid,sensors,10)}")

#part 2
def Part2(sensors,grid):
    sensorsRange = []
    for s in sensors:
        sensorsRange.append(ClosestBeacon(s[0],s[1],beacons)[1])
    for y in range(0,4000001):
        x=0
        while x <4000001:
            a = 0
            for i,s in enumerate(sensors):
                
                if Manhattan(x,y,s[0],s[1]) > sensorsRange[i]:
                    a+=1
                else:
                    x=s[0]+ (sensorsRange[i]-abs(s[1]-y))
                    break

            if a==len(sensorsRange):
                return (x,y)
            x+=1        
p2 = Part2(sensors,grid)
print(f"part 2: {(p2[0]*4000000)+p2[1]}")