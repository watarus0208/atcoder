N = int(input())
S = input()

l = S[0]
for i in range(N):
    if l[-1] != S[i]:
        l += S[i]

print(len(l))