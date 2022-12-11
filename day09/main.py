with open("input.txt") as f:
    l = f.read().splitlines()

step={"R":[0,+1],"L":[0,-1],"U":[-1,0],"D":[+1,0]}
def Part1(l):
    has_been={(0,0)}
    hx,hy,tx,ty = 0,0,0,0
    for x in l:
        d,n = x.split(' ')
        n= int(n)
        dx,dy = step[d]
        for i in range(n):
            hx += dx
            hy += dy
            while max(abs(tx - hx), abs(ty - hy)) > 1:
                if abs(tx - hx) > 0:
                    if hx > tx:
                        tx += 1 
                    else: 
                        tx -= 1
                if abs(ty - hy) > 0:
                    if hy > ty:
                        ty += 1 
                    else: 
                        ty -= 1
                has_been.add((tx, ty))
    return len(has_been)

def Part2(l):
    rope = [(0,0)]*10
    seen = set()
    
    for x in l:
        d,n = x.split(' ')
        n= int(n)
        dx,dy = step[d]
        for _ in range(n):
            hx, hy = rope[0]
            rope[0] = hx + dx, hy + dy
            for i in range(1,10):
                px, py = rope[i - 1]
                kx, ky = rope[i]
                while max(abs(kx - px), abs(ky - py)) > 1:
                    if abs(kx - px) > 0:
                        if px > kx:
                            kx += 1 
                        else: 
                            kx -= 1
                    if abs(ky - py) > 0:
                        if py > ky:
                            ky += 1 
                        else: 
                             ky -= 1
                rope[i]=kx,ky
            seen.add(rope[9])
    return len(seen)
    


print(f"part 1: {Part1(l)}")
print(f"part 2: {Part2(l)}")