N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(N):
    if A[i] >= B[i]:
        A[i] = 0
        B[i] = 