s = input()
n = len(s)

ans = 10**10
for i in range(2**n):
    tmp = ''
    for j in range(n):
        if ((i >>j) & 1):
            tmp = tmp+s[j] 
    if tmp!='' and int(tmp)%3==0:
        ans = min(ans, n - len(tmp))
if ans == 10**10:
    print(-1)
else:
    print(ans)