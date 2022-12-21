N = int(input())
S = input()

ans = ''
n = 0
while n < N:
    if S[n] == '"':
        i = n+1
        while i < N:
            if S[i] == '"':
                ans += S[n:i+1]
                # print(ans)
                break
            i += 1
        n = i+1
    else:
        j = n
        while j < N:
            if j == N-1 or S[j+1] == '"':
                ans += S[n:j+1].replace(',', '.')
                # print(ans)
                break
            j += 1
        n = j+1

print(ans)