S = input()
T = input()

cnt = 0
for i in range(len(S)):
    if S[i] != T[i]:
        print(i+1)
        break
else:
    print(len(T))