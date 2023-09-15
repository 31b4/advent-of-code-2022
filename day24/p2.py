from math import lcm
from heapq import heappop, heappush
import copy
import time

# -5: # -4: right -3: left -2: down -1: up 0: space 1,2,3 ect: occupy
def ReadAll():
    with open("input.txt") as f:
        grid = []
        for line in f.readlines():
            grid.append(list(line.strip()))
    return grid

class Bliz:
    def __init__(self, y, x, dir):
        self.x = int(x)
        self.y = int(y)
        self.dir = dir


def Move(blizzard, grid):
    # 0>
    # 1v
    # 2<
    # 3^
    if blizzard.dir == 0:
        if blizzard.x == len(grid[0])-2:
            blizzard.x = 1
        else:
            blizzard.x += 1
    elif blizzard.dir == 2:
        if blizzard.x == 1:
            blizzard.x = len(grid[0])-2
        else:
            blizzard.x -= 1
    elif blizzard.dir == 1:
        if blizzard.y == len(grid) - 2:
            blizzard.y = 1
        else:
            blizzard.y += 1
    elif blizzard.dir == 3:
        if blizzard.y == 1:
            blizzard.y = len(grid) - 2
        else:
            blizzard.y -= 1
    #print("asdasdasdasdasda ", blizzard.y,blizzard.x,blizzard.dir)
    return blizzard


def PrintGrid(grid):
    for line in grid:
        print("".join(line))
    print("")

def BlizzardsMove(grid, blizzards):
    bliz2 =[]
    for b in blizzards:
        grid[b.y][b.x] = '.'
        b = Move(b, grid)
        bliz2.append(b)
        # grid[b.y][b.x] = b.dir #edit grid
    for b in blizzards:
        n = 0
        for b2 in blizzards:
            if b.x == b2.x and b.y == b2.y:
                n += 1
        if n > 1:
            grid[b.y][b.x] = str(n)
        else:
            grid[b.y][b.x] = b.dir

    return grid, bliz2

def FMove(F,grid,blizzards,time):
    time +=1
    grid, blizzards = BlizzardsMove(grid,blizzards)
    for d in [[1,0],[0,1],[-1,0],[0,-1], [0,0]]:
        if grid[F.y+ d[0]][F.x + d[1]] == '.':
            grid[F.y][F.x] = '.'
            F.y = F.y+ d[0]
            F.x = F.x + d[1]
            grid[F.y][F.x] = 'F'
            break
    #PrintGrid(grid)
    if F.y == len(grid)-1 and F.x == len(grid[0])-2:
        print("part 1: ",time)
        PrintGrid(grid)
        exit(0)
    return F, grid, blizzards, time

def Occupied(loc, st):
    print()
    for d in range(4):
        sv = Bliz(loc[0], loc[1], d)
        #print(f"     ({sv.y}, {sv.x}, {sv.dir})")

        for x in st:
            if sv.y == x.y and sv.x == x.x and sv.dir == x.dir:
                print("asd")
                return True
        if sv in st:
            print("asd")
            return True
    return False

def PathFinder(states,n,m,period):
    start = (0,1)
    end = (n-1,m-2)
    pq = [(0, start, False, False)]
    visited = set()
    while len(pq) > 0:
        top = heappop(pq)
        if top in visited:
            continue
        visited.add(top)
        t, loc, hit_end, hit_start = top
        row, col = loc

        assert not (hit_start and not hit_end)
        assert not Occupied(loc, states[t % period])
        print(loc)
        if loc == end:
            if hit_end and hit_start:
                return t

            hit_end = True

        if loc == start:
            if hit_end:
                hit_start = True
            # Go through neighbors

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for drow, dcol in (dirs + [[0, 0]]):
            new_row, new_col = row + drow, col + dcol
            new_loc = (new_row, new_col)

            # Within bounds?
            if (not new_loc in [start, end]) \
                    and not (1 <= new_row <= n - 2
                             and 1 <= new_col <= m - 2):
                continue

            # Check if hitting a blizzard
            if Occupied(new_loc, states[(t + 1) % period]):
                continue

            new_state = (t + 1, new_loc, hit_end, hit_start)
            heappush(pq, new_state)



def Part1(grid):
    

    blizzards = []
    for y,line in enumerate(grid):
        for x,e in enumerate(line):
            if e in ">v<^":
                blizzard = Bliz(y,x,">v<^".index(e))
                blizzards.append(blizzard)
    F = Bliz(0,1,'F')
    time = 0
    #while True:
    #    F,grid,blizzards,time = FMove(F,grid,blizzards,time)

    period = lcm(len(grid)-2, len(grid[0])-2)
    states = []
    sv_blizzards = copy.deepcopy(blizzards)
    states.append(sv_blizzards)

    print(states[0][0].y, states[0][0].x, states[0][0].dir)

    for t in range(1, period):
        grid, blizzards = BlizzardsMove(grid, blizzards)
        #print(t)
        sv_blizzards = copy.deepcopy(blizzards)
        states.append((sv_blizzards))
    #print(states[0][0].y, states[0][0].x, states[0][0].dir)
    print(PathFinder(states, len(grid), len(grid[0]),period))


if __name__ == '__main__':
    start_time = time.time()

    grid = ReadAll()
    Part1(grid)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

