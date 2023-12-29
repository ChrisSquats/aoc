with open("2023-day-9-input.txt", "r") as f:
    lines = [[*map(int,line.split())] for line in f] # new skill, * is for unpacking object, equivalent to list() in this case

ans = []
ans2 = []
#lines = [lines[200-1]]
for reading in lines:
    delta = reading.copy()
    #print(*reading)
    extrap = reading[-1]
    extrap2 = reading[0]
    while any(delta):
        delta=[*map(lambda x,y: (y-x), delta[:-1], delta[1:])]
        extrap += delta[-1]
        extrap2 -= delta[0] * ((-1) ** (len(delta)))
        #print(*delta)
    #print(f'extrap: {extrap} back strap: {extrap2}\n')
    ans.append(extrap)
    ans2.append(extrap2)
print(sum(ans),sum(ans2))