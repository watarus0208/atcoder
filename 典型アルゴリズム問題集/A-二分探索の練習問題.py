N, K = map(int, input().split())
A = list(map(int, input().split()))

if A[N-1] < K:
    print(-1)
    exit()

l, r = 0, N
while l+1<r:
    m = (l+r)//2
    # 条件を満たす場合
    if K <= A[m]:
        r = m
    # 条件を満たさない場合
    else:
        l = m

print(r)