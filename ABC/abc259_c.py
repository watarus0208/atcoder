S = input()
T = input()

cnt = 0
for i, s in enumerate(S):
    if i == 0:
        if S[0] != T[0]:
            print('No')
            exit()
    elif S[i-1] == S[i]:
        j = i 
        cnt = 1 
        while True:
            if T[j] == T[j+cnt]:
                cnt += 1

                