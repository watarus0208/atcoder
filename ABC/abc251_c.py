from collections import defaultdict

N = int(input())

d = defaultdict(int)
l = []
for n in range(N):
    s, t = input().split()
    l.append(s)
    if s in d:
        continue
    else:
        d[s] = int(t)

max_s = max(d, key=d.get)
print(l.index(max_s)+1)