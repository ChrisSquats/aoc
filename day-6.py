import math
T = [40, 82, 91, 66]
D = [277, 1338, 1349, 1063]

#T = [7, 15, 30]
#D = [9, 40, 200]
T = [int(''.join(map(str,T)))]
D = [int(''.join(map(str,D)))]
ans=1
a = -1
i=0
for i in range(len(T)):
    d = T[i]**2-4*a*-D[i] # discriminant
    
    if d < 0:
        print ("This equation has no real solution")
    elif d == 0:
        x = (-T[i]+math.sqrt(d))/2*a
        ans += 1
    else:
        x1 = (-T[i]+math.sqrt(d))/(2*a)
        if x1 == int(x1): x1 += 1
        x2 = (-T[i]-math.sqrt(d))/(2*a)
        if x2 == int(x2): x2 -= 1
        #print(math.floor(x2), math.ceil(x1),x2-x1+1, x1 == int(x1))
        ans *= (math.floor(x2)-math.ceil(x1)+1)
    i+=1
print(ans)