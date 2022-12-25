n = int(input())
a = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    d = list(map(int, input().split()))
    if d[0] == 1:
        k = d[1]-1
        a[k] = d[2]
    else:
        k = d[1]-1
        print(a[k])