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
PrintMap(map)
# GO GO GO GO GOOO

dirs = [-1,0],[0,1],[1,0],[0,-1] #up,right,down,left
dir = 0
pos = start

for cmd in commads:
    turn, step = cmd
    print(cmd)
    print(turn,step)
    if turn == 'R':
        dir = (dir +1)%4
    elif turn == 'L':
        dir = (dir -1)%4
    for i in range(step): # lepesek
        newx = (pos[0] + dirs[dir][0]) % height
        newy = (pos[1] + dirs[dir][1]) % width# top bottom left right border done
        if map[newx][newy] == '.':
            map[newx][newy] = 'A'
            map[pos[0]][pos[1]] = '.'
            pos = [newx,newy]
            #PrintMap(map)
            #print()
        elif map[newx][newy] == ',': # if blank step
            sv_newx = (newx + dirs[dir][0]) % height
            sv_newy = (newy + dirs[dir][1]) % width
            while map[sv_newx][sv_newy] == ',':
                #print(sv_newx,sv_newy)
                #print((sv_newx + dirs[dir][1]) )
                sv_newx = (sv_newx + dirs[dir][0]) % height
                sv_newy = (sv_newy + dirs[dir][1]) % width
            if map[sv_newx][sv_newy] == '.':
                print(sv_newx)
                print(sv_newy)
                map[sv_newx][sv_newy] = 'A'
                map[pos[0]][pos[1]] = '.'
                pos = [sv_newx, sv_newy]
                #PrintMap(map)
            elif map[sv_newx][sv_newy] == '#':
                continue

if dir == 0:
    dir = 3
else:
    dir -= 1

ans = 1000*(pos[0]+1) + 4* (pos[1]+1) + ((dir)%4)
print(ans)


