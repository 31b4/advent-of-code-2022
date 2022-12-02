with open('input.txt') as f:
    lines = f.read().splitlines()
lines = [x.split(" ") for x in lines]
print(lines)
ans = 0
elf =["A","B","C"]
me =["X","Y","Z"]
score = 0
for x in lines:
    e = elf.index(x[0])
    m = me.index(x[1])
    if e==m:
        score += m+1+3
    elif e== 1 and m == 0:
        score += m+1
    elif e== 0 and m == 1:
      score += m+1+6
    elif e== 2 and m == 1:
      score += m+1
    elif e== 0 and m == 2:
        score+= m+1
    elif e== 1 and m == 2:
        score+= m+1+6
    elif e== 2 and m == 0:
        score+= m+1+6
    elif e== 1 and m == 0:
        score+= m+1

print("part 1: ",score)


score2=0
scores = {'A': 1, 'B': 2, 'C': 3}
final_score = {
    'AA': 3,
    'BB': 3,
    'CC': 3,
    'AB': 6,
    'BC': 6,
    'CA': 6,
    'AC': 0,
    'BA': 0,
    'CB': 0
}
convert = {
    'AY': 'A',
    'BX': 'A',
    'CZ': 'A',
    'AZ': 'B',
    'BY': 'B',
    'CX': 'B',
    'AX': 'C',
    'BZ': 'C',
    'CY': 'C'
}
for x in lines:
    e = x[0]
    m = x[1]
    converted = convert[e+m]
    forChoose = scores[converted]
    final_final_score = final_score[e+converted]
    score2+=forChoose+final_final_score
print("part 2:",score2)