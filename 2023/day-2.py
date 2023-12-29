with open("2023-day-2-input.txt", "r") as f:
    lines = [line.strip() for line in f]
    
import re
maxr = 12
maxg = 13
maxb = 14
games = []
ans = 0
for l in lines:
    reds = [int(x) for x in re.findall(r'(\d+) red',l)]
    greens = [int(x) for x in re.findall(r'(\d+) green',l)]
    blues = [int(x) for x in re.findall(r'(\d+) blue',l)]
    game = int(re.findall(r'(\d+):',l)[0])
    
    if (max(reds) <= maxr) & (max(greens) <= maxg) & (max(blues) <= maxb):
        games.append(game)
    ans += max(reds) * max(greens) * max(blues)
print(sum(games))
print(ans)