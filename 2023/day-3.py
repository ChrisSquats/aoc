with open("2023-day-3-input.txt", "r") as f:
    lines = [line.strip() for line in f]
    
import re

#get symbols
syms = []
nums = []

#print([(x.span(),int(x.group())) for x in re.finditer(r'\d+',lines[0])])
#seq = [(x.group(), i, x.span()[0]) for x in re.finditer(r'\D|\.',lines[1])]
#print(list(filter(lambda x: x[0] != '.', seq)))
for i,l in enumerate(lines):
    num = [(int(x.group()), i, x.span()) for x in re.finditer(r'\d+',l)]
    if num:
        nums.extend(num)
    sym = [(x.group(), i, x.span()[0]) for x in re.finditer(r'\D',l)]
    
    sym = list(filter(lambda x: x[0] != '.', sym)) # remove .
    if sym:
        syms.extend(sym)
ans = 0
#print(nums,syms)
for num in nums:
    #print('working on ',num)
    for d in range(num[2][0],num[2][1]):
        dp = (num[1] ,d)
        #print('dp', dp)
        for sym in syms:
            if  (dp[0] + 1 == sym[1] and dp[1] == sym[2]) or (dp[0] - 1 == sym[1] and dp[1] == sym[2]) or (dp[0] == sym[1] and dp[1] + 1 == sym[2]) or (dp[0] == sym[1] and dp[1] - 1 == sym[2]) or (dp[0] + 1 == sym[1] and dp[1] + 1 == sym[2]) or (dp[0] + 1 == sym[1] and dp[1] - 1 == sym[2]) or (dp[0] - 1 == sym[1] and dp[1] + 1 == sym[2]) or (dp[0] - 1 == sym[1] and dp[1] - 1 == sym[2]) :
                #print('adding ' ,num[0])
                ans+=num[0]
                #print('number found')
                break
        else:
            #print('herenow')    
            continue
        break    

    
        
print(ans)

stars = list(filter(lambda x: x[0]=="*",syms))
print(stars)