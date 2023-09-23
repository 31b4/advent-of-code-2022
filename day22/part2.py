with open('input.txt') as f:
    lines = f.read().split("\n\n")
command = lines[1]
commads = []
step = ""
LorR = "R" #staring pos is looking up so with R turn firt its gonna look to the right dir
for x in command:
    if x != 'L' and x != 'R':
        step +=x # stringkent hozzacsatolja
    else:
        commads.append((LorR, int(step)))
        step = ""
        LorR = x
commads.append((LorR, int(step)))

print("commands: ",commads)
map = []

width = max(len(lines[0].split("\n")[0]), len(lines[0].split("\n")[-1]))  # elso sor hossza (main input)

 # utolso sor hossza (test input)


for l in lines[0].split("\n"):# create the map replace blank with -1
    sv = ["," for _ in range(width)]
    for i,x in enumerate(l):
        if x == ' ':
            continue
        sv[i] = x
    map.append(sv)

height = len(map)
print(height)
print(width)
start = []# find the start position
for i,x in enumerate(map[0]):
    if x == '.':
        start = [0,i]
        break
print("start: ",start)

# 0: (0) up
# 1: (90) right
# 2: (180) down
# 3: (270) left
# if L dir-- if R dir++
# keplet: dir % 4
def PrintMap(map):
    for x in map:
        print("".join(x))
# GO GO GO GO GOOO

dirs = [-1,0],[0,1],[1,0],[0,-1] #up,right,down,left
dir = 0
pos = start

for cmd in commads:
    turn, step = cmd

    if turn == 'R':
        dir = (dir +1)%4
    elif turn == 'L':
        dir = (dir -1)%4
    for i in range(step): # lepesek
        newx = 0
        newy = 0
        #-----PINK-----
        if pos[0] == 0 and pos[1] > 99 and dir == 0:
            newx = height-1
            newy = pos[1]-100
        elif pos[0] == height-1 and dir == 2:
            newx = 0
            newy = 100 + pos[1]
        #-----PURPLE-----
        elif pos[0] == 0 and pos[1] < 100 and dir == 0:
            newx = 150 + pos[1]-50
            newy = 0
            if map[newx][newy] != '#':
                dir = (dir + 1) % 4
        elif pos[1] == 0 and pos[0] > 149 and dir == 3:
            newx = 0
            newy = 50 + pos[0]-150
            if map[newx][newy] == '.':
                dir = (dir - 1) % 4
        # -----YELLOW-----
        elif pos[1] == 50 and pos[0] < 50 and dir == 3:
            newx = 149 - pos[0]
            newy = 0
            if map[newx][newy] == '.':
                dir = (dir +2) % 4
        elif pos[1] == 0 and pos[0] < 150 and dir == 3:
            newx = 49 - (pos[0]-100)
            newy = 50
            if map[newx][newy] == '.':
                dir = (dir +2) % 4
        # -----BLUE-----
        elif pos[1] == 50 and 49 < pos[0] < 100 and dir == 3:
            newx = 100
            newy = pos[0]-50
            if map[newx][newy] == '.':
                dir = (dir -1) % 4
        elif pos[0] == 100 and pos[1] < 50 and dir == 0:
            newx = 50 + pos[1]
            newy = 50
            if map[newx][newy] == '.':
                dir = (dir +1) % 4
        # -----BLACK-----
        elif pos[0] == 49 and pos[1] > 99 and dir == 2:
            newx = 50 + pos[1]-100
            newy = 99
            if map[newx][newy] == '.':
                dir = (dir +1) % 4
        elif pos[1] == 99 and 49 < pos[0] < 100 and dir ==1:
            newx = 49
            newy = 100 + pos[0]-50
            if map[newx][newy] == '.':
                dir = (dir -1) % 4
        # -----ORANGE-----
        elif pos[1] == width-1 and dir == 1:
            newx = 149 - pos[0]
            newy = 99
            if map[newx][newy] == '.':
                dir = (dir +2) % 4
        elif pos[1] == 99 and pos[0] > 99 and dir == 1:
            newx = 49 - (pos[0]-100)
            newy = width-1
            if map[newx][newy] == '.':
                dir = (dir +2) % 4
        # -----GREY-----
        elif pos[0] == 149 and pos[1] > 49 and dir == 2:
            newx = 150 + pos[1]-50
            newy = 49
            if map[newx][newy] == '.':
                dir = (dir +1) % 4
        elif pos[1] == 49 and pos[0] > 149 and dir == 1:
            newx = 149
            newy = 50 + pos[0]-150
            if map[newx][newy] == '.':
                dir = (dir -1) % 4
        else:
            newx = (pos[0] + dirs[dir][0])
            newy = (pos[1] + dirs[dir][1])

        print(newx,newy)

        if map[newx][newy] == '.':
            map[newx][newy] = 'A'
            map[pos[0]][pos[1]] = '.'
            pos = [newx,newy]
if dir == 0:
    dir = 3
else:
    dir -= 1
print(pos[0])
print(pos[1])
print(dir%4)
ans = 1000*(pos[0]+1) + 4* (pos[1]+1) + ((dir)%4)
print(ans)

