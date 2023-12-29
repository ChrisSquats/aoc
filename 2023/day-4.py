with open("2023-day-4-input.txt", "r") as f:
    lines = [line.strip().split('|') for line in f]
    
import re
#print(lines)

ans = 0
ans2 = [1 for i in range(len(lines))]
i=1
for line in lines:
    win = re.findall(r'\d+',line[0])[1:]
    card = re.findall(r'\d+',line[1])
    m = set(win)&set(card)
    if m:
        ans += 2 ** (len(m)-1)
        for j in range(i,i+len(m)):
            ans2[j] += ans2[i-1]
    i+=1
    
print(ans)
print(sum(ans2))

