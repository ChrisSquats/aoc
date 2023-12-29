from collections import Counter

with open("2023-day-7-input.txt", "r") as f:
    lines = [line.strip().split(' ') for line in f]
#print(lines, len(lines))
numhands = len(lines)
order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
typez = ['hc','1p','2p','3k','fh','4k','5k']
typez.reverse()

handType = {k: list() for k in typez} #create container for hands

for hand in lines:
    h = Counter(hand[0]).most_common(5)
    h_lessJ = list(filter(lambda x: x[0]  != 'J',h))
    
    if len(h_lessJ) > 0: t1 = h_lessJ[0][1] #count the most common not J because it messes with stuff like JJJKK
    if len(h_lessJ) > 1: t2 = h_lessJ[1][1]
    j = [x[1] for x in h if x[0] == 'J'] # count how many Js
    if len(j) > 0 : j=j[0] 
    print(hand,t1,t2,j)
    if t1 == 5 or j==5 or (t1 == 4 and j == 1) or (t1 ==3 and j ==2) or (t1 == 2 and j ==3) or (t1 == 1 and j ==4): #5k
        handType['5k'].append(hand)
    elif t1 == 4 or (t1 == 3 and j == 1) or (t1 == 2 and j == 2) or (t1 == 1 and j == 3): #4k
        handType['4k'].append(hand)
    elif t1 == 3 and t2 ==2 or (t1 == 2 and t2 == 2 and j == 1): #fh 
        handType['fh'].append(hand) 
    elif t1 == 3 and t2 == 1 or (t1 == 2 and t2 == 1 and j == 1) or (t1 == 1 and t2 == 1 and j == 2): #3k AAKQJ QT6JJ
        handType['3k'].append(hand)
    elif t1 == 2 and t2 == 2: #2p AAKQJ
        handType['2p'].append(hand)
    elif t1 == 2 and t2 == 1 or (t1 == 1 and j == 1) : #1p 2345J
        handType['1p'].append(hand)
    else:
        handType['hc'].append(hand)
    
print(handType)
ans = 0
for k,v in handType.items():
    handType[k].sort(key = lambda ele: [order.index(c) for c in list(ele[0])])
    #print(handType[k])
    for i in handType[k]:
        ans+=int(i[1])*numhands
        numhands-=1
print(ans)