N = int(input())
A = [int(input()) for _ in range(N)]

amax = max(A)

for i in range(N):
    if A[i] != amax:
        print(amax)
    else:
        print(max(A[:i] + A[i+1:]))
