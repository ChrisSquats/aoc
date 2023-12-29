with open("2023/Inputs/2023-day-11-input.txt", "r") as f:
    lines = [[*line.strip()] for line in f]

import numpy as np
#print(lines)
a = np.array(lines)

#print(a)
universe = a.copy()
#print(universe)
num_expansions_x = 0
num_expansions_y = 0

exp_x =[]
exp_y = []
age_factor = 999999
for i,l in enumerate(a):
    if '#' not in l:
        #print('expansion needed',i,l)
        num_expansions_x += 1
        exp_x.append(i)
        universe = np.insert(universe,i+num_expansions_x,'.',axis = 0)
    if '#' not in universe[:,i+num_expansions_y]:
        #print('expansion needed y')
        num_expansions_y += 1
        exp_y.append(i)
        universe = np.insert(universe,i+num_expansions_y,'.',axis = 1)

print(exp_y, exp_x)
#print(universe,universe.shape)
print(list(zip(*np.where(universe == '#'))))
galaxies = [(i+1, x[0],x[1]) for i,x in enumerate(zip(*np.where(universe == '#')))]
#print(galaxies)
galaxies2 = [(i+1, x[0],x[1]) for i,x in enumerate(zip(*np.where(a == '#')))]
print(a)
print(galaxies2)
for i,g in enumerate(galaxies2):
    offset_x = age_factor*len([j for j in exp_x if j <= g[1]])
    offset_y = age_factor*len([k for k in exp_y if k <= g[2]])
    galaxies2[i] = (g[0],g[1]+offset_x,g[2]+offset_y)
print(galaxies2)
dist = []
for i,g1 in enumerate(galaxies2[:-1]):
    for g2 in galaxies2[i+1:]:
        dist.append(abs(g1[1]-g2[1])+abs(g1[2]-g2[2]))
print(sum(dist))











''' old method pre numpy
#expand universe
universe_x = lines.copy()
num_exp = 0
for i,l in enumerate(lines):
    if l.find('#') < 0:
        print('expansion needed',i)
        num_exp += 1
        universe_x.insert(i+num_exp,l)

universe = universe_x.copy()
num_exp = 0

#print(''.join(list(zip(*universe_x))))

for i,l_t in enumerate(zip(*universe_x)):
    l = ''.join(l_t)
    if l.find('#') < 0:
        print('expansion needed',i)
        num_exp += 1
        universe.insert(i+num_exp,l)

print(universe)
'''