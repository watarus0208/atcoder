S = input()
T = input()

if len(S) > len(T):
    print('No')
    exit()

i = 0
while i<len(S):
    if S[i] != T[i]:
        if T[i-2] == T[i-1] == T[i]:
            T = T[:i-1] + T[i:]
        else:
            print('No')
            exit()
    else:
        i += 1
if S == T:
    print('Yes')
else:
    print('No')