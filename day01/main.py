with open('input.txt') as f:
    lines = f.read().split("\n\n")
lines = [x.split("\n") for x in lines]
part1 = 0
part2 = 0
asd = []
for x in lines:
    asd.append(sum(list(map(int,x))))
part1 = max(asd)

asd= sorted(asd)
asd.reverse()    
part2= asd[0]+asd[1]+asd[2]


print(f"part 1: {part1}")
print(f"part 1: {part2}")





