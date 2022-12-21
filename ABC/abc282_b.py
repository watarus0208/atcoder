N, M = map(int, input().split())
S = [input() for _ in range(N)]

cnt = 0
for n in range(N-1):
    n_ = n+1
    while n_ < N:
        for m in range(M) :
            if S[n][m]=='x' and S[n_][m]=='x':
                break
        else:
            cnt += 1
        # print(S[n], n)
        # print(S[n_], n_)
        n_ += 1

print(cnt)