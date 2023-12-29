import re
with open("2023-day-1-input.txt", "r") as f:
    lines = [line.strip() for line in f]
ans = 0
for l in lines:
    #print(l)
    break
    nums = re.findall('\d',l)
    #print(nums)
    num = int(nums[0]+nums[-1])
    #print(num)
    ans += num
    
#print(ans)
#transform txt to number
ans2=0
numString = {"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
q = 1
for l in lines:
    numSpan = []
    numSpan.extend([[x.span(),x.group()] for x in re.finditer(r'\d',l)])
    for i,s in numString.items():
        
        if re.search(s,l):
            #numSpan.append([re.search(s,l).span(),i])
            numSpan.extend([[x.span(),i] for x in re.finditer(s, l)])
    numSpan.sort() #sort so that i know which number is first and last
    if numSpan:
        #replace the first and last with the number
        l = l.replace(numString[numSpan[0][1]],numSpan[0][1])
        l = l.replace(numString[numSpan[-1][1]],numSpan[-1][1])
    print(l)
    
    print(numSpan)
    num = int(numSpan[0][1]+numSpan[-1][1])
    print(q, num)
    q += 1
    ans2 += num
print(ans2)