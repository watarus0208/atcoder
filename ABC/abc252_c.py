from collections import defaultdict

N = int(input())
S = [input() for _ in range(N)]

d = defaultdict(int)
for n in range(N):
    for i in range(10):
        print(S[:][i])
        d[S[n][i]] = max(i, d[S[n][i]])
print(min(d.values()))