import string
with open("input.txt") as f:
    lines = f.read().splitlines()
g= [list(l) for l in lines]
n = len(g)
m = len(g[0])
sx,sy = [(i,j) for i in range(n) for j in range(m) if g[i][j] == "S"][0]
tx,ty = [(i,j) for i in range(n) for j in range(m) if g[i][j] == "E"][0]


print(tx,ty)
