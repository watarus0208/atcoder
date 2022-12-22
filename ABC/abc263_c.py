N, M = map(int, input().split())

ans = []
i = 1

def p(l, j):
    if len(l) == N:
        print(l)
    else:
        while (len(l)==0 or l[-1] < j) and len(l)<N:
            l.append(j)
            j += 1
            print(l, j)
            p(l, j)

print(p(ans, i))