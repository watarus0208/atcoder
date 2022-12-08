import bisect

inf = 10*18

N, M = map(int, input().split())
A = sorted(map(int, input().split()))
B = [-inf] + sorted(map(int, input().split())) + [inf]

B.append(inf)
B.insert(0, -inf)

ans = inf
for a in A:
    i = bisect.bisect_right(B,a)
    # l = 0
    # r = len(B)
    # while l+1 < r:
    #     m = (l+r)//2
    #     if a - B[m] < 0:
    #         r = m
    #     else:
    #         l = m
    # ans = min(ans, a-B[l], B[r]-a)
    ans = min (ans, a-B[i-1], B[i]-a)

print(ans)