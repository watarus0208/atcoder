N, T = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
total = sum(A)
T_ = T%total
for a in A:
    # print(a)
    cnt += 1
    T_ -= a
    # print(T)
    if T_ < 0:
        print(N if cnt%N==0 else cnt%N, T_+a)
        exit()