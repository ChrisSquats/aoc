with open("2023-day-5-input.txt", "r") as f:
    lines = [line.strip() for line in f]
import re

seeds = [int(x) for x in re.findall(r'\d+', str(lines[0]))]
##P2 Start
seeds = [[seeds[i],seeds[i+1]] for i in range(0,len(seeds),2)]
seeds2 = []
for seed in seeds:
    seeds2.append([x for x in range(seed[0],seed[1])])
print(seeds)

##P2 end
maps = ['s2s','s2f','f2w','w2l','l2t','t2h','h2l']
zmap = {k:[] for k in maps}

for line in lines[3:]:
    if line == '':
        continue
    elif re.findall(r'map',line):
        maps.pop(0)
        continue
    zmap[maps[0]].append([int(x) for x in re.findall(r'\d+', line)])
          

#print(zmap)
ans=[]
for seed in seeds:
    for k,v in zmap.items():
        for r in v:
            if r[1] <= seed <= (r[1] + r[2]):
                seed = r[0] - r[1] + seed
                #print('seed moved to', seed, r)
                break
        else:
            pass
            #print('range not found', seed)
    ans.append(seed)
print(min(ans))