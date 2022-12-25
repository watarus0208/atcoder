from collections import defaultdict

N, Q = map(int, input().split())

m = defaultdict(set)

for q in range(Q):
    ac, u1, u2  = map(int, input().split())
    if ac==1:
        m[u1].add(u2)
    elif ac==2:
        m[u1].discard(u2)
    elif ac==3:
        if u1 in m[u2] and u2 in m[u1]:
            print('Yes')
        else:
            print('No')