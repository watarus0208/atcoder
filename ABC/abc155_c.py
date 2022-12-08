from collections import defaultdict

N = int(input())
S = [input() for _ in range(N)]

d = defaultdict(int)

for key in S:
    d[key] += 1
max_v = max(d.values())

L = sorted([key for key in d if d.get(key)==max_v])

for l in L:
    print(l)