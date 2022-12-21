N = int(input())
S = input()

ans = ''
out = True

for i in range(N):
    if S[i]=='"':
        out = not out
    if out and S[i] == '.':
        ans += '.'
    else:
        ans += S[i]

print(ans)