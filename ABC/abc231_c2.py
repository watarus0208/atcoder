n, q = map(int, input().split())
a = sorted(list(map(int, input().split())))

"""クエリ先読み"""
l = []
for i in range(q):
    l.append([int(input()), i])
l.sort()
ans = [0]*q
j = 0
for x, i in l:
    while j < n and a[j] < x:
        j += 1
    ans[i] = n-j

print(*ans)