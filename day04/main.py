
with open("input.txt") as f:
    data = f.read().splitlines()
data = [x.split(",") for x in data]
db=0
for x in data:
    x[0] = x[0].split('-')
    x[1] = x[1].split('-')
    if int(x[0][0])>= int(x[1][0]) and int(x[0][1]) <= int(x[1][1]):
        db+=1
    elif int(x[1][0])>= int(x[0][0]) and int(x[1][1]) <= int(x[0][1]):
        db+=1
print(f"part 1: {db}")

db=0
for x in data:
    if int(x[0][0])>= int(x[1][0]) and int(x[0][1]) <= int(x[1][1]):
        db+=1
    elif int(x[1][0])>= int(x[0][0]) and int(x[1][1]) <= int(x[0][1]):
        db+=1
    elif int(x[0][0])>= int(x[1][0]) and int(x[0][0])<= int(x[1][1]):
        db+=1
    elif int(x[0][1])>= int(x[1][0]) and int(x[0][1])<= int(x[1][1]):
        db+=1
    elif int(x[1][0])>= int(x[0][0]) and int(x[1][0])<= int(x[0][1]):
        db+=1
    elif int(x[1][1])>= int(x[0][0]) and int(x[1][1])<= int(x[0][1]):
        db+=1
    
    
print(f"part 2: {db}")