
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
    if blizzard.dir == '>':
        if blizzard.x == len(grid[0])-2:
            blizzard.x = 1
        else:
            blizzard.x += 1
    elif blizzard.dir == '<':
        if blizzard.x == 1:
            blizzard.x = len(grid[0])-2
        else:
            blizzard.x -= 1
    elif blizzard.dir == 'v':
        if blizzard.y == len(grid) - 2:
            blizzard.y = 1
        else:
            blizzard.y += 1
    elif blizzard.dir == '^':
        if blizzard.y == 1:
            blizzard.y = len(grid) - 2
        else:
            blizzard.y -= 1
    return blizzard
def Part1(grid):
    blizzards = []
    for y,line in enumerate(grid):
        for x,e in enumerate(line):
            if e in ['^','v','<','>']:
                blizzard = Bliz(y,x,e)
                blizzards.append(blizzard)

    for i in range(5):
        for b in blizzards:

            grid[b.y][b.x] = '.'
            b = Move(b, grid)
            grid[b.y][b.x] = b.dir
        for line in grid:
            print("".join(line))
        print("")
    # eloszor lefutnak a lepesek es utanna iratom ki hogy ki hol van, ahol tobben
    # vannak ott db szamot irok
if __name__ == '__main__':
    grid = ReadAll()
    Part1(grid)

