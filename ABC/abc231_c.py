n, q = map(int, input().split())
a = sorted(list(map(int, input().split())))

for _ in range(q):
    x = int(input())
    if x < a[0]:
        print(n)
        continue
    if x > a[n-1]:
        print(0)
        continue
    i = 0
    l = 0
    r = len(a)
    while r-l > 1:
        i = (l+r)//2
        if a[i] >= x:
            r = i
        else:
            l = i 
    print(n - r)
    