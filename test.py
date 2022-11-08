N, M = map(int, input().split())
common = []
for i in range(N):
    if i==0:
        common = list(map(int, input().split()))[1:]
        print('i==0')
        print(common)
    else:
        tmp = list(map(int, input().split()))[1:]
        for j, c in enumerate(common):
            if c not in tmp:
                common.pop(j)
                print(i)
                print(common)

print(len(common))