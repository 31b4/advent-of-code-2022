import os
clear = lambda: os.system('cls')

def ReadSave():
    bottom = 0
    grid = {}
    input = open('input.txt').read()
    for ln in input.split("\n"):
        places = ln.split(" -> ")
        places = [tuple(map(int, x.split(","))) for x in places]
        x, y = places[0]
        bottom = max(bottom, y)
        grid[x, y] = "#"
        for nx, ny in places[1:]:
            while x != nx or y != ny:
                dx = (nx > x) - (x > nx)
                dy = (ny > y) - (y > ny)
                x = x + dx
                y = y + dy
                grid[x, y] = "#"
                bottom = max(bottom, y)
            x == nx
            y == ny
    return grid,bottom

def DrawGrid(grid):
    clear()
    for y in range(100):
        for x in range(330, 680):
            if grid.get((x,y)) == 'o':
                print("o",end="")
            else:
                print("#" if (x, y) in grid else ".", end="")
        print()
    print()

def Solve(grid,bottom):
    part1 = True
    bottom = bottom + 2
    for x in range(-1000, 1000):
        grid[x, bottom] = "#"
    t=0
    p1 = 0
    while True:
        if not part1 and p1 == 0: 
            p1 = t-1
            DrawGrid(grid)
        sx, sy = 500, 0
        if grid.get((sx, sy)) == "o":
            break
        
        while True:
            #DrawGrid(grid)
            if  sy == bottom-1 and part1: 
                part1= False #ha erinti az aljat akkor p1 vege
                
            if grid.get((sx, sy + 1), None) is None:
                sy = sy + 1 # lefele
                continue

            elif grid.get((sx - 1, sy + 1), None) is None:
                sx = sx - 1 # balra
                sy = sy + 1
                continue

            elif grid.get((sx + 1, sy + 1), None) is None:
                sx = sx + 1 # jobbra
                sy = sy + 1
                continue

            else: #ha beszorul
                grid[(sx, sy)] = "o"
                t+=1
                break     
    return p1,sum(1 for k, v in grid.items() if v == "o")

grid,bottom = ReadSave()
print(Solve(grid,bottom))
