H, W = map(int, input().split())

L = [input() for _ in range(H)]
C = [[0]*W for _ in range(H)]

i = j = 0
while 1:
    if C[i][j]:
        print(-1)
        break

    C[i][j] = 1

    if L[i][j] == 'U':
        if i == 0:
            break
        i -= 1
    elif L[i][j] == 'D':
        if i == H-1:
            break
        i += 1
    elif L[i][j] == 'L':
        if j == 0:
            break
        j -= 1
    elif L[i][j] == 'R':
        if j == W-1:
            break
        j += 1

print(i+1, j+1)