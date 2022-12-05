N = int(input())
S = list(map(int, input().split()))

ans = []
for n in range(N):
    if n == 0:
        ans.append(S[0])
    else:
        ans.append(S[n]-S[n-1])

print(*ans)