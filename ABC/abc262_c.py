import math

N = int(input())
a = list(map(int, input().split()))

cnta=0
cntb=0
for i in range(N):
    if a[i] == i+1:
        cnta += 1
    if a[a[i]-1]==i+1:
        cntb += 1
cntb -= cnta
print(math.comb(cnta, 2)+int(cntb/2))