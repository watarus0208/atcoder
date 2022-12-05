N, M = map(int, input().split())
fav = [0]*M
for _ in range(N):
    KA = list(map(int, input().split()))
    for a in range(KA[0]):
        fav[KA[a+1]-1] += 1
print(fav)
