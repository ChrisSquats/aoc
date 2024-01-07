with open("2023/Inputs/2023-day-12-input.txt", "r") as f:
    lines = [line.strip() for line in f]

cache = {}
'''def searchRecords(record,dmg,i,j,k):
    #i = current char
    #j = current dmg length
    #k is keeping track of the length of #
    ans_local = 0
    key = (record,dmg,i,j,k)

    
    if i == len(record): 
        if j == len(dmg) and k == 0:
            #print(record)
            return 1
        elif j == len(dmg)-1 and k == dmg[j]:
            #print(record)
            return 1
        else:
            return 0
    elif j > len(dmg):
        return 0
    
    if key in cache:
        return cache[key]

    if record[i] == '.':
        if k == dmg[j if j<len(dmg) else j-1]:
            ans_local += searchRecords(record,dmg,i+1,j+1,0)
        elif 0 < k < dmg[j if j<len(dmg) else j-1]: #save a few stacks by exiting if k is less than dmg
            return 0
        else:
            ans_local += searchRecords(record,dmg,i+1,j,0)
    elif record[i] == '#':
        if k >= dmg[j if j<len(dmg) else j-1]: # save more stacks
            return 0
        ans_local += searchRecords(record,dmg,i+1,j,k+1)
    elif record[i] == '?':
        for c in ['.','#']:
            record_new = record.replace('?',c,1)
            ans_local += searchRecords(record_new,dmg,i,j,k)
            #cache.pop(key)
    cache[key] = ans_local
    return ans_local'''

def searchRecords(record,dmg):
    ans_local = 0
    key = (record,dmg)
    if key in cache:
        return cache[key]
    if record == "":
        return 1 if dmg == () else 0
    if dmg == ():
        return 0 if "#" in record else 1

    if record[0] in ".?": # treat ? like a dot in this case
        ans_local += searchRecords(record[1:],dmg)
    
    if record[0] in "#?": #treat ? like a #
        # Start of a spring
        # condition 1: there are enough springs left
        # condition 2: all spings in this block must be broken
        # condition 3: next spring after must be the length of record OR a working spring
        if len(record) >= dmg[0] and "." not in record[:dmg[0]] and (len(record) == dmg[0] or record[dmg[0]] != "#"):
            ans_local += searchRecords(record[dmg[0]+1:],dmg[1:]) # the +1 is very important and is stops another block forming
    cache[key] = ans_local
    return ans_local

ans = 0

for i,l in enumerate(lines):
    record, dmg = l.split()
    #print('input',i, l)

    dmg = tuple([int(x) for x in dmg.split(',')])
    record = '?'.join([record]*5)
    dmg *= 5
    ans += searchRecords(record,dmg)#,0,0,0)
    cache.clear()
print(ans)

