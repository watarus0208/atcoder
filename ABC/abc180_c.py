import math

n = int(input())
lst = []

for i in range(1, int(math.sqrt(n))+1):
    if n%i==0:
        lst.extend([i, int(n/i)])
ans = set(lst)
for a in sorted(ans):
    print(a)