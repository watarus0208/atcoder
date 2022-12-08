N, M = map(int, input().split())

L = []
R = []
for m in range(M):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

ans = min(R) - max(L) + 1

if ans <= 0:
    print(0)
else:
    print(ans)