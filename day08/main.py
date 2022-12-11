with open("input.txt") as f:
    grid = []
    for line in f.readlines():
        grid.append(list(map(int, line.strip())))
dir=[(-1, 0), (1, 0), (0, -1), (0, 1)]
def solve_part_1(grid):
    res = 0
    m = len(grid)
    n = len(grid[0])
    def isVisible(i, j):
        for x, y in dir:
            xi, yj = i+x, j+y
            while 0 <= xi < m and 0 <= yj < n and grid[xi][yj] < grid[i][j]:
                xi += x
                yj += y
            if not (0 <= xi < m and 0 <= yj < n):
                return True
        return False
    for i in range(m):
        for j in range(n):
            if isVisible(i, j):
                res += 1
    return res

def solve_part_2(grid):
    res = 0
    m = len(grid)
    n = len(grid[0])
    def isVisible(i, j):
        s=1
        dir=[(-1, 0), (1, 0), (0, -1), (0, 1)]
        for x, y in dir:
            xi, yj = i+x, j+y
            curr = 0
            while 0 <= xi < m and 0 <= yj < n:
                curr += 1
                if grid[xi][yj] >= grid[i][j]:
                    break
                xi += x
                yj += y

            s*=curr
        return s
    for i in range(m):
        for j in range(n):
            res = max(res,isVisible(i,j))
    return res

print(f"part 1: {solve_part_1(grid)}")
print(f"part 2: {solve_part_2(grid)}")