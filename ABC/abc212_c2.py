inf = 10*18

N, M = map(int, input().split())
A = sorted(map(int, input().split()))
B = [-inf]+sorted(map(int, input().split())) + [inf]

ans = inf
i = 0
for a in A:
    # B[i] < a <= B[i+1] になるまでiを増やす
    while B[i+1] < a: i += 1
    ans = min(ans, a-B[i], B[i+1]-a)

print(ans)