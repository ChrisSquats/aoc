with open("2023/Inputs/2023-day-10-input.txt", "r") as f:
    lines = f.readlines()
#print(lines)
for y,l in enumerate(lines):
    if (x:=l.find('S')) >= 0: break

print(x,y)
pos = lines[y][x]
path = [(pos,x,y)]
while True:
    #print(path)
    if pos == 'S' and len(path) > 1:
        break
    if (pos:=lines[y-1][x]) in ['F','7','|'] and ((pos,x,y-1) not in path):
        path.append((pos,x,y-1))
        y = y - 1
        #continue
    elif (pos:=lines[y+1][x]) in ['L','J','|'] and ((pos,x,y+1) not in path):
        path.append((pos,x,y+1))
        y = y + 1
        #continue
    elif (pos:=lines[y][x-1]) in ['L','F','-'] and ((pos,x-1,y) not in path):
        path.append((pos,x-1,y))
        x = x - 1
        #continue
    elif (pos:=lines[y][x+1]) in ['7','J','-'] and ((pos,x+1,y) not in path):
        path.append((pos,x+1,y))
        x = x + 1
        #continue
    break

while True:
    print(path[-1])
    if path[-1][0] == '|':
        if (pos:=(lines[y+1][x],x,y+1)) not in path:
            y+=1
            path.append(pos)
            continue
        elif (pos2:=(lines[y-1][x],x,y-1)) not in path:
            y-=1
            path.append(pos2)
            continue
    elif path[-1][0] == 'L':
        if (pos:=(lines[y][x+1],x+1,y)) not in path:
            x+=1
            path.append(pos)
            continue
        elif (pos2:=(lines[y-1][x],x,y-1)) not in path:
            y-=1
            path.append(pos2)
            continue
    elif path[-1][0] == '-':
        if (pos:=(lines[y][x+1],x+1,y)) not in path:
            x+=1
            path.append(pos)
            continue
        elif (pos2:=(lines[y][x-1],x-1,y)) not in path:
            x-=1
            path.append(pos2)
            continue
    elif path[-1][0] == 'J':
        if (pos:=(lines[y][x-1],x-1,y)) not in path:
            x-=1
            path.append(pos)
            continue
        elif (pos2:=(lines[y-1][x],x,y-1)) not in path:
            y-=1
            path.append(pos2)
            continue
    elif path[-1][0] == '7':
        if (pos:=(lines[y][x-1],x-1,y)) not in path:
            x-=1
            path.append(pos)
            continue
        elif (pos2:=(lines[y+1][x],x,y+1)) not in path:
            y+=1
            path.append(pos2)    
            continue
    elif path[-1][0] == 'F':
        if (pos:=(lines[y][x+1],x+1,y)) not in path:
            x+=1
            path.append(pos)
            continue
        elif (pos2:=(lines[y+1][x],x,y+1)) not in path:
            y+=1
            path.append(pos2)    
            continue
    break
    

print(len(path) // 2)
path = [(p[1],p[2]) for p in path]

zmap = []
for x in range(len(lines[0])-1):
    for y in range(len(lines)):
        p = (x,y)
        if p not in path:
            zmap.append((x,y))

print(zmap)
ans = []
for p in zmap:
    i = 0
    edges = 0
    print('looking at',p,ans)
    while True:
        pl = (p[0]-i,p[1])
        pr = (p[0]+i,p[1])
        print(pl, edges)
        if (pl[0] == 0) or (pl[0] == len(lines[0])-2) :
            break
        elif pr[0] == len(lines[0])-1:
            edges = 0
            break
        elif pl in path:
            edges += 1
            i += 1

        elif ((pl[0],pl[1]+1) in ans) or ((pl[0],pl[1]-1) in ans) or ((pl[0]+1,pl[1]) in ans) or ((pl[0]-1,pl[1]) in ans):
            if pl not in ans:
                ans.append(pl)
            break
        elif pl not in path:
            i+=1
        else:
            print('Wtf')
        
    if edges % 2 != 0:
        ans.append(p)
    print(ans)
print(ans,len(ans))
print(zmap)