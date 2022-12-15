l = open("input.txt").read().splitlines()

def ReadSave():
    sensors = []
    beacons= []
    grid={}
    for line in l:
        sx, sy, bx, by = map(int, re.findall(r'(?<=\=)(.*?)(?=,|\:|\n)', line))
        sensors.append((sx,sy))
        beacons.append((bx,by))
        grid[(sx,sy)]= 'S'
        grid[(bx,by)]= 'B'
    return sensors,beacons

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

sensors,beacons,grid = ReadSave()

