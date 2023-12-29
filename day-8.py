import re
import math
from functools import reduce

with open("2023-day-8-input.txt", "r") as f:
    data = f.read()
    starts = re.findall(r'(\w\wA)\s',data)
    ends = re.findall(r'(\w\wZ)\s',data)
    lines = re.split(r'\n',data)
steps = lines[0]
#print(starts, ends, lines)
#p = re.compile(r'(\w{3}).*(\w{3}).*(\w{3})')
p = re.compile(r'(\w{3})')

zmap = {}
for l in lines[2:]:
    path = p.findall(l)
    zmap[path[0]] = [path[1], path[2]]
    
#print(zmap)

'''c = 'AAA'
ans = 0
i=0
while i < len(steps):
    if steps[i] == 'L':
        c = zmap[c][0] 
    else:
        c = zmap[c][1] 
    ans+=1
    if c == 'ZZZ':
        break
    steps += steps[i]
    i+=1
print(ans) '''   

#### p2
positions = starts
ans2=0
i=0
a=[]
while i < len(steps):
    for j,position in enumerate(positions):
        if steps[i] == 'L':
            positions[j] = zmap[position][0] 
        else:
            positions[j] = zmap[position][1] 
    ans2+=1
    boolPos = [x[-1] == 'Z' for x in positions]
    
    if any(boolPos):
        print(boolPos,ans2)
        a.append(ans2)
        if len(a) == len(starts): #this is not correct, it's lucky that in this case the cycles don't overlap
            
            print(reduce(lambda x,y:(x*y)//math.gcd(x,y),a))
            # math: LCM(a,b) = a × b / GCD(a,b)
            break
    steps += steps[i]
    i+=1
    #print(positions,boolPos,ans2)  
    