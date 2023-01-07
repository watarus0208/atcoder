from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
cnt = 1 
d[1] = 0
print(d[1])
for a in A:
    if a in d.keys():
        d[cnt+1] = d[a]+1
        d[cnt+2] = d[a]+1
        print(d[cnt+1])
        print(d[cnt+2])
        cnt += 2 