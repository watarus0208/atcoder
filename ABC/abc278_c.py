N, Q = map(int, input().split())

m = [[0]*N for i in range(N)]
for q in range(Q):
    ac, u1, u2  = map(int, input().split())
    if ac==1:
        m[u1-1][u2-1] = 1 
    elif ac==2:
        m[u1-1][u2-1] = 0 
    elif ac==3:
        if m[u1-1][u2-1] == m[u2-1][u1-1] == 1:
            print('Yes')
        else:
            print('No')