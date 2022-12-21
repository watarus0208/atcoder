n, q = map(int,input().split())
s = input()
i = 0
for _ in range(q):
    t, x = map(int, input().split())
    if t==1:
        i = (i+x)%n
    else:
        print(s[x-i-1])
