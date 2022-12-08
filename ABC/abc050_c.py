N = int(input())
T = list(map(int, input().split()))
M = int(input())

for m in range(M):
    P, X = map(int, input().split())
    tmp = T[P-1]
    T[P-1] = X
    print(sum(T))
    T[P-1] = tmp