N, M = map(int, input().split())

d = {}
for n in range(N):
    A, B = map(int, input().split())
    if A in d:
        d[A] += B
    else:
        d[A] = B

# from collections import defaultdict
# d = defaultdict(int)
# d[A]+=B

sum = 0
ans = 0
for key in sorted(d.keys()):
    sum += d[key]
    ans += key*d[key]
    if M < sum:
        ans = ans - (sum - M)*key
        break

print(ans)
