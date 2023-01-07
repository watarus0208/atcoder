n = int(input())
a = list(map(int, input().split()))

e = []
o = []

for i in range(n):
    if a[i]%2==0:
        e.append(a[i])
    else:
        o.append(a[i])

e.sort()
o.sort()

if len(o)>=2 and len(e)>=2:
    ans = max(e[-1]+e[-2], o[-1]+o[-2])
elif len(o)>=2 and len(e)<2:
    ans = o[-1]+o[-2]
elif len(o)<2 and len(e)>=2:
    ans = e[-1]+e[-2]
else:
    ans = -1

"""
ans = -1
if len(o)>1: ans=max()
if len(e)>1: ans=max()
"""

print(ans)