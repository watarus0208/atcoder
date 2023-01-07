from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
B = sorted(set(A))

d = defaultdict(int)

for a in A: 
    j  = len(B) - B.index(a) -1
    d[j] += 1

for i in range(n):
    print(d[i])